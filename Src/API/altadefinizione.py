"""AltaDefinizione metadata and renewing HLS relay for Stremio clients."""
import asyncio
import base64
import html
import json
import os
import re
import time
from html.parser import HTMLParser
from urllib.parse import urljoin, urlsplit, urlunsplit, parse_qsl, urlencode

import httpx
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import Response
import Src.Utilities.config as config

router = APIRouter()
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
SESSIONS = {}
MAX_SESSIONS = 256
MAX_RESOURCE = 32 * 1024 * 1024


class AsyncSession(httpx.AsyncClient):
    """Use the same ordinary HTTP transport verified by the download service."""
    async def get(self, url, **kwargs):
        kwargs['follow_redirects'] = kwargs.pop('allow_redirects', True)
        return await super().get(url, **kwargs)


class Scripts(HTMLParser):
    def __init__(self):
        super().__init__(); self.active = False; self.items = []; self.current = ''
    def handle_starttag(self, tag, attrs):
        if tag == 'script': self.active = True; self.current = ''
    def handle_data(self, data):
        if self.active: self.current += data
    def handle_endtag(self, tag):
        if tag == 'script' and self.active:
            self.items.append(self.current); self.active = False


def extract_player(document, metadata=None):
    parser = Scripts(); parser.feed(document)
    for script in parser.items:
        source = script
        match = re.search(r"(?:var|let|const)\s+\w+\s*=\s*(['\"])([^'\"]+)\1\s*,\s*\w+\s*=\s*atob\(\s*(['\"])([A-Za-z0-9+/=]+)\3\s*\)", script)
        if match:
            key = match[2].encode()
            data = base64.b64decode(match[4], validate=True)
            source = bytes(v ^ key[i % len(key)] for i,v in enumerate(data)).decode()
        source = source.replace('\\/', '/')
        match = re.search(r'''(?:currentSrc|file|source)\s*["']?\s*[:=]\s*["'](https?://[^"']+)["']''', source)
        if not match: match = re.search(r'''(https?://[^\s"'<>]+\.m3u8(?:\?[^\s"'<>]*)?)''', source)
        if match:
            url = html.unescape(match[1])
            if urlsplit(url).scheme in ('http','https'):
                if metadata is not None:
                    metadata['subtitles']=[]
                    subs=re.search(r'window\.__EXTERNAL_SUBS\s*=\s*(\[.*?\])\s*;',source,re.S)
                    origin=re.search(r'''window\.__SUBS_ORIGIN\s*=\s*["']([^"']+)["']''',source)
                    if subs and origin:
                        try:
                            for item in json.loads(subs[1]):
                                lang=item.get('lang')
                                target=urljoin(origin[1],item.get('url',''))
                                if lang and urlsplit(target).scheme in ('http','https'):
                                    metadata['subtitles'].append({'id':str(lang)+('-forced' if item.get('forced') else ''),'lang':str(lang),'url':target})
                        except (ValueError,TypeError,AttributeError):pass
                return url
    return None


def valid_id(value):
    if not re.fullmatch(r'tt\d+(?::\d+:\d+)?', value):
        raise HTTPException(400, 'Identificativo non valido')
    return value


def media_headers():
    origin = config.VD_DOMAIN.rstrip('/')
    return {'User-Agent': UA, 'Referer': origin+'/', 'Origin': origin, 'Accept':'*/*', 'Sec-Fetch-Dest':'empty', 'Sec-Fetch-Mode':'cors', 'Sec-Fetch-Site':'cross-site'}


async def resolve_player(stream_id, client, metadata=None):
    valid_id(stream_id)
    parts = stream_id.split(':')
    path = parts[0][2:] if len(parts)==1 else '/'.join(parts)
    referer = os.getenv('ALTADEFINIZIONE_URL','https://altadefinizionex.life').rstrip('/')+'/'
    response = await client.get(config.VD_DOMAIN.rstrip('/')+'/'+path, headers={
        'User-Agent':UA, 'Referer':referer, 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Sec-Fetch-Dest':'iframe', 'Sec-Fetch-Mode':'navigate', 'Sec-Fetch-Site':'cross-site', 'Cache-Control':'no-cache'}, timeout=30, allow_redirects=True)
    if response.status_code != 200: raise HTTPException(502,'Player AltaDefinizione non disponibile')
    if len(response.content)>2*1024*1024: raise HTTPException(502,'Risposta player troppo grande')
    url = extract_player(response.text,metadata)
    if not url: raise HTTPException(502,'Flusso AltaDefinizione non trovato')
    return url


class Session:
    def __init__(self, stream_id):
        self.stream_id=stream_id; self.url=None; self.until=0; self.touched=time.monotonic(); self.lock=asyncio.Lock(); self.subtitles=[]

    async def fresh(self, client, force=False, previous=None):
        async with self.lock:
            if previous and previous!=self.url: return
            if not force and self.url and time.monotonic()<self.until: return
            metadata={}
            self.url=await resolve_player(self.stream_id,client,metadata)
            self.subtitles=metadata.get('subtitles',[])
            # Signatures currently expire in milliseconds; use a short fallback for other formats.
            ttl=60.0
            query=dict(parse_qsl(urlsplit(self.url).query))
            try: ttl=min(60.0,max(1.0,float(query['e'])/1000-time.time()-30))
            except (KeyError,ValueError): pass
            self.until=time.monotonic()+ttl


def session_for(stream_id):
    valid_id(stream_id)
    if stream_id not in SESSIONS:
        if len(SESSIONS)>=MAX_SESSIONS:
            oldest=min(SESSIONS,key=lambda k:SESSIONS[k].touched)
            SESSIONS.pop(oldest)
        SESSIONS[stream_id]=Session(stream_id)
    session=SESSIONS[stream_id];session.touched=time.monotonic()
    return session


def resource_token(target, master):
    target=urlsplit(target);base=urlsplit(master)
    directory=base.path.rsplit('/',1)[0]+'/'
    if target.netloc!=base.netloc or not target.path.startswith(directory):
        raise HTTPException(502,'Risorsa HLS fuori dal percorso del flusso')
    relative=target.path[len(directory):]
    if not relative or '..' in relative.split('/') or len(relative)>512: raise HTTPException(502,'Percorso HLS non valido')
    query=[(k,v) for k,v in parse_qsl(target.query,keep_blank_values=True) if k not in ('t','e')]
    data=json.dumps({'p':relative,'q':query},separators=(',',':')).encode()
    return base64.urlsafe_b64encode(data).decode().rstrip('=')


def resource_url(token, master):
    if len(token)>4096: raise HTTPException(400,'Risorsa non valida')
    try:
        data=json.loads(base64.urlsafe_b64decode(token+'='*(-len(token)%4)))
        path=data['p'];query=data['q']
        if not isinstance(path,str) or not re.fullmatch(r'[A-Za-z0-9_./-]{1,512}',path) or path.startswith('/') or '..' in path.split('/'):
            raise ValueError()
        if not isinstance(query,list) or len(query)>20 or any(not isinstance(p,list) or len(p)!=2 or not all(isinstance(v,str) for v in p) for p in query): raise ValueError()
        if any(k in ('t','e') for k,v in query): raise ValueError()
    except Exception: raise HTTPException(400,'Risorsa non valida')
    base=urlsplit(master)
    signed=[(k,v) for k,v in parse_qsl(base.query) if k in ('t','e')]
    return urlunsplit((base.scheme,base.netloc,base.path.rsplit('/',1)[0]+'/'+path,urlencode([tuple(pair) for pair in query]+signed),''))


def relay_link(request, stream_id, quality, token):
    data=json.loads(base64.urlsafe_b64decode(token+'='*(-len(token)%4)))
    filename=data['p'].rsplit('/',1)[-1]
    url=request.url_for('alta_resource',stream_id=stream_id,quality=quality,token=token,filename=filename)
    scheme=request.headers.get('x-forwarded-proto',url.scheme).split(',')[0].strip()
    return str(url.replace(scheme=scheme if scheme in ('http','https') else url.scheme))


def rewrite_playlist(text, source, master, request, stream_id, quality):
    if not text.startswith('#EXTM3U'): raise HTTPException(502,'Playlist HLS non valida')
    lines=text.splitlines();output=[];skip=False
    for line in lines:
        if line.startswith('#EXT-X-I-FRAME-STREAM-INF:') and quality!='best':
            height=re.search(r'RESOLUTION=\d+x(\d+)',line)
            if not height or height[1]!=quality:continue
        if line.startswith('#EXT-X-STREAM-INF:'):
            height=re.search(r'RESOLUTION=\d+x(\d+)',line)
            skip=quality!='best' and (not height or height[1]!=quality)
            if skip: continue
        elif line and not line.startswith('#'):
            if skip: skip=False;continue
            token=resource_token(urljoin(source,line),master)
            line=relay_link(request,stream_id,quality,token)
        elif 'URI="' in line:
            def replace(match):
                token=resource_token(urljoin(source,match[1]),master)
                return 'URI="'+relay_link(request,stream_id,quality,token)+'"'
            line=re.sub(r'URI="([^"]+)"',replace,line)
        output.append(line)
    if '#EXT-X-VERSION:' not in text: output.insert(1,'#EXT-X-VERSION:6')
    return '\n'.join(output)+'\n'


async def fetch_resource(client, session, token=None, byte_range=None):
    for attempt in range(2):
        await session.fresh(client)
        previous=session.url
        url=resource_url(token,previous) if token else previous
        headers=media_headers()
        if byte_range: headers['Range']=byte_range
        response=await client.get(url,headers=headers,timeout=40,allow_redirects=True)
        if response.status_code in (401,403) and attempt==0:
            await session.fresh(client,force=True,previous=previous)
            continue
        if response.status_code not in (200,206): raise HTTPException(502,'Risorsa AltaDefinizione temporaneamente non disponibile')
        if len(response.content)>MAX_RESOURCE: raise HTTPException(502,'Risorsa HLS troppo grande')
        return response,url
    raise HTTPException(502,'Flusso scaduto')


@router.get('/alta/{stream_id}/{quality}/manifest.m3u8',name='alta_manifest')
async def alta_manifest(request:Request,stream_id:str,quality:str):
    if not re.fullmatch(r'best|[1-9]\d{2,3}',quality): raise HTTPException(400,'Qualita non valida')
    session=session_for(stream_id)
    async with AsyncSession() as client:
        response,source=await fetch_resource(client,session)
    text=rewrite_playlist(response.text,source,session.url,request,stream_id,quality)
    return Response(text,media_type='application/vnd.apple.mpegurl',headers={'Cache-Control':'no-store','Access-Control-Allow-Origin':'*'})


@router.get('/alta/{stream_id}/{quality}/resource/{token}',name='alta_resource_legacy',include_in_schema=False)
@router.get('/alta/{stream_id}/{quality}/resource/{token}/{filename}',name='alta_resource')
async def alta_resource(request:Request,stream_id:str,quality:str,token:str,filename:str|None=None):
    if not re.fullmatch(r'best|[1-9]\d{2,3}',quality): raise HTTPException(400,'Qualita non valida')
    session=session_for(stream_id)
    byte_range=request.headers.get('range')
    if byte_range and not re.fullmatch(r'bytes=(?:\d+-\d*|-\d+)',byte_range): raise HTTPException(416)
    async with AsyncSession() as client:
        response,source=await fetch_resource(client,session,token,byte_range)
    headers={'Cache-Control':'no-store','Access-Control-Allow-Origin':'*','Accept-Ranges':'bytes'}
    if response.headers.get('content-range'):headers['Content-Range']=response.headers['content-range']
    if response.content.startswith(b'#EXTM3U'):
        content=rewrite_playlist(response.text,source,session.url,request,stream_id,quality)
        return Response(content,media_type='application/vnd.apple.mpegurl',headers=headers)
    if not response.content: raise HTTPException(502,'Segmento vuoto')
    return Response(response.content,status_code=response.status_code,media_type=response.headers.get('content-type','application/octet-stream'),headers=headers)


async def alta_streams(streams, stream_id, client, instance_url):
    session=session_for(stream_id)
    async with AsyncSession() as relay:
        await session.fresh(relay)
        response,source=await fetch_resource(relay,session)
    if not response.text.startswith('#EXTM3U'):return streams
    heights=sorted({int(v) for v in re.findall(r'^#EXT-X-STREAM-INF:[^\r\n]*RESOLUTION=\d+x(\d+)',response.text,re.M)},reverse=True)
    language_names={'it':'Italiano','ita':'Italiano','en':'Inglese','eng':'Inglese','fr':'Francese','fra':'Francese','de':'Tedesco','deu':'Tedesco','es':'Spagnolo','spa':'Spagnolo'}
    languages=[]
    for line in response.text.splitlines():
        if line.startswith('#EXT-X-MEDIA:') and 'TYPE=AUDIO' in line:
            language=re.search(r'LANGUAGE="([^"]+)"',line)
            if language:
                code=language[1].lower()
                if code not in ('und','') and code not in languages:languages.append(code)
    audio=', '.join(language_names.get(code,code) for code in languages) or 'lingua non dichiarata'
    for height in heights or ['best']:
        quality=f'{height}p' if isinstance(height,int) else 'Qualita non dichiarata'
        title=f'AltaDefinizione · {quality}\nAudio: {audio}\nVidxgo'
        streams['streams'].append({'name':f'{config.Name} · AltaDefinizione\n{quality}', 'title':title,'description':title,
            'url':instance_url.rstrip('/')+f'/alta/{stream_id}/{height}/manifest.m3u8',
            'behaviorHints':{'notWebReady':True,'bingeGroup':f'altadefinizione-{height}'},'subtitles':session.subtitles})
    return streams
