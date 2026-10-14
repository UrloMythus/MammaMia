import asyncio
import base64
import json
import time
import unittest
from unittest.mock import AsyncMock, patch
from urllib.parse import urlsplit,parse_qs
from starlette.requests import Request
from fastapi import HTTPException
from Src.API import altadefinizione as alta
import run


def request(path='/test'):
    return Request({'type':'http','method':'GET','path':path,'raw_path':path.encode(),'query_string':b'',
        'scheme':'http','server':('testserver',8080),'client':('127.0.0.1',1),'headers':[], 'app':run.app,'router':run.app.router,'root_path':''})


async def call_app(path):
    sent=[]
    async def receive():return {'type':'http.request','body':b'','more_body':False}
    async def send(message):sent.append(message)
    scope=dict(request(path).scope);scope['http_version']='1.1'
    await run.app(scope,receive,send)
    status=next(m['status'] for m in sent if m['type']=='http.response.start')
    body=b''.join(m.get('body',b'') for m in sent if m['type']=='http.response.body')
    return status,json.loads(body)


class Response:
    def __init__(self,code,content,headers=None):
        self.status_code=code;self.content=content;self.text=content.decode(errors='replace');self.headers=headers or {}


class AltaTests(unittest.IsolatedAsyncioTestCase):
    def test_player_metadata(self):
        source=b'window.currentSrc="https://cdn.example/hls/42/master.m3u8?t=secret&e=99&b=5";'
        key=b'ab';data=base64.b64encode(bytes(v^key[i%2] for i,v in enumerate(source))).decode()
        document=f"<script>var c='ab',d=atob('{data}');</script>"
        self.assertEqual(alta.extract_player(document),'https://cdn.example/hls/42/master.m3u8?t=secret&e=99&b=5')
        self.assertIsNone(alta.extract_player('<script>window.currentSrc="file:///etc/passwd"</script>'))
        metadata={}
        document='<script>window.currentSrc="https://cdn.example/master.m3u8";window.__EXTERNAL_SUBS=[{"lang":"ita","url":"italian.vtt","forced":true}];window.__SUBS_ORIGIN="https://subs.example/";</script>'
        alta.extract_player(document,metadata)
        self.assertEqual(metadata['subtitles'],[{'id':'ita-forced','lang':'ita','url':'https://subs.example/italian.vtt'}])

    async def test_live_tv_source_name(self):
        config=base64.b64encode(b'|LIVETV|').decode()
        status,data=await call_app(f'/{config}/stream/tv/rai-1.json')
        self.assertEqual(status,200)
        self.assertTrue(data['streams'])
        self.assertTrue(all('LiveTV' in s['name'] for s in data['streams']))

    def test_rewrite_all_hls_uris_and_quality(self):
        master='https://cdn.example/hls/42/master.m3u8?t=old&e=1&b=5'
        text='#EXTM3U\n#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="a",URI="audio.m3u8?t=old&e=1&b=3"\n#EXT-X-STREAM-INF:BANDWIDTH=1,RESOLUTION=1920x1080\nv1080.m3u8?t=old&e=1&b=5\n#EXT-X-STREAM-INF:BANDWIDTH=1,RESOLUTION=1280x720\nv720.m3u8?t=old&e=1&b=2\n'
        result=alta.rewrite_playlist(text,master,master,request(),'tt42','1080')
        self.assertNotIn('cdn.example',result)
        self.assertNotIn('t=old',result)
        self.assertNotIn('1280x720',result)
        self.assertIn('1920x1080',result)
        self.assertIn('/alta/tt42/1080/resource/',result)
        self.assertIn('#EXT-X-VERSION:6',result)
        media='#EXTM3U\n#EXT-X-KEY:METHOD=AES-128,URI="key.bin"\n#EXT-X-MAP:URI="init.mp4"\n#EXTINF:6,\nseg.ts?t=old&e=1&b=20\n#EXT-X-ENDLIST'
        result=alta.rewrite_playlist(media,master,master,request(),'tt42','1080')
        self.assertEqual(result.count('/resource/'),3)

    def test_resource_scope_and_signed_query(self):
        old='https://cdn.example/hls/42/master.m3u8?t=old&e=1&b=5'
        target='https://cdn.example/hls/42/seg-1.ts?t=old&e=1&b=123'
        token=alta.resource_token(target,old)
        renewed=alta.resource_url(token,'https://new-cdn.example/hls/42/master.m3u8?t=new&e=999&b=5')
        self.assertEqual(urlsplit(renewed).hostname,'new-cdn.example')
        self.assertEqual(parse_qs(urlsplit(renewed).query),{'b':['123'],'t':['new'],'e':['999']})
        with self.assertRaises(HTTPException):alta.resource_token('http://127.0.0.1/admin',old)
        for path in ['../admin','/etc/passwd','https://evil.example/file']:
            bad=base64.urlsafe_b64encode(json.dumps({'p':path,'q':[]}).encode()).decode().rstrip('=')
            with self.assertRaises(HTTPException):alta.resource_url(bad,old)

    def test_relay_urls_keep_extensions_and_https(self):
        master='https://cdn.example/hls/42/master.m3u8?t=old&e=1&b=5'
        token=alta.resource_token('https://cdn.example/hls/42/seg.ts?t=old&e=1&b=1',master)
        scope=dict(request().scope);scope['headers']=[(b'x-forwarded-proto',b'https')]
        result=alta.relay_link(Request(scope),'tt42','1080',token)
        self.assertTrue(result.startswith('https://testserver:8080/alta/'))
        self.assertTrue(result.endswith('/seg.ts'))

    async def test_vlc_only_resolves_streamingcommunity(self):
        from fastapi.responses import JSONResponse
        response=JSONResponse({'streams':[{'name':'MammaMia · StreamingCommunity TV Proxy','url':'https://proxy.example/test.m3u8'}]})
        client=AsyncMock();client.get.return_value=Response(200,b'#EXTM3U\n#EXT-X-ENDLIST\n')
        context=AsyncMock();context.__aenter__.return_value=client
        with patch.object(run,'addon_stream',AsyncMock(return_value=response)) as resolver,patch.object(run,'AsyncSession',return_value=context):
            await run.vlc_stream(request('/vlc/movie/tt42.m3u8'),'movie','tt42')
        codes=base64.b64decode(resolver.call_args.kwargs['config']).decode()
        self.assertIn('AD_OFF',codes)

    async def test_expiry_refresh_and_range(self):
        session=alta.Session('tt42');session.url='https://cdn.example/hls/42/master.m3u8?t=old&e=1&b=5';session.until=time.monotonic()+60
        token=alta.resource_token('https://cdn.example/hls/42/seg.ts?t=old&e=1&b=50',session.url)
        client=AsyncMock();client.get.side_effect=[Response(403,b'forbidden'),Response(206,b'segment',{'content-range':'bytes 0-6/7'})]
        new='https://cdn.example/hls/42/master.m3u8?t=new&e=9999999999999&b=5'
        with patch.object(alta,'resolve_player',AsyncMock(return_value=new)) as resolve:
            result,url=await alta.fetch_resource(client,session,token,'bytes=0-6')
        self.assertEqual(result.status_code,206)
        self.assertIn('t=new',url)
        self.assertEqual(resolve.await_count,1)
        self.assertEqual(client.get.call_args.kwargs['headers']['Range'],'bytes=0-6')

    async def test_provider_names_legacy_and_opt_out(self):
        async def sc(streams,*args):
            streams['streams'].append({'name':'MammaMia TV Proxy','title':'StreamingCommunity','url':'https://proxy.example/manifest.m3u8'})
            return streams
        async def ad(streams,*args):
            streams['streams'].append({'name':'MammaMia','title':'AltaDefinizione','url':'https://alta.example/manifest.m3u8'})
            return streams
        with patch.object(run,'SC','1'),patch.object(run,'VD','1'),patch.object(run,'streaming_community',sc),patch.object(run,'vidxgoalta',ad):
            for codes,expected in [('|SC|LIVETV|',2),('|SC|AD_OFF|',1),('|VD|',1),('|AD|',1)]:
                config=base64.b64encode(codes.encode()).decode()
                status,data=await call_app(f'/{config}/stream/movie/tt42.json')
                self.assertEqual(status,200)
                self.assertEqual(len(data['streams']),expected)
                for stream in data['streams']:
                    label='StreamingCommunity' if 'StreamingCommunity' in stream['title'] else 'AltaDefinizione'
                    self.assertIn(label,stream['name'])
                    self.assertEqual(stream['description'],stream['title'])
                    if label=='StreamingCommunity':
                        self.assertTrue(stream['name'].endswith(' TV Proxy'))
                        self.assertIn('/vlc/movie/tt42.m3u8',stream['url'])


if __name__=='__main__':unittest.main()
