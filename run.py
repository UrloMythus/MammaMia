from fastapi import FastAPI, HTTPException,Request, Form,Cookie
from fastapi.responses import JSONResponse,RedirectResponse,HTMLResponse,Response
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from static.static import HTML
from static.configure import  CONFIGURE
from fastapi.templating import Jinja2Templates
from  Src.API.streamingcommunity import streaming_community
from Src.API.cb01 import cb01
from Src.API.guardaserie import guardaserie
from Src.API.guardahd import guardahd
from Src.API.animeworld import animeworld
from Src.API.guardaflix import guardaflix
from Src.API.guardoserie import guardoserie
from Src.API.eurostreaming import eurostreaming
from  Src.API.onlineserietv import onlineserietv
from  Src.API.vidxgoalta import vidxgoalta
from Src.API.altadefinizione import router as alta_router
from Src.API.toonitalia import toonitalia
from Src.API.realtime import search_catalog as realtime
from Src.API.realtime import meta_catalog as meta_catalog_realtime
from Src.API.realtime import realtime as streams_realtime
from Src.Utilities.dictionaries import STREAM,extra_sources,provider_map
from Src.Utilities.update_config import update_all_sites
from Src.API.epg import tivu, tivu_get,epg_guide,convert_bho_1,convert_bho_2,convert_bho_3
from Src.API.extractors.uprot import get_uprot_numbers,generate_uprot_txt
import logging
from urllib.parse import unquote, quote
from curl_cffi.requests import AsyncSession
import base64
from copy import deepcopy
import json
import  Src.Utilities.config as config
from Src.Utilities.config import setup_logging
level = config.LEVEL
logger = setup_logging(level)
from Src.Utilities.loadenv import load_env
env_vars = load_env()
from Src.Utilities.manifest import router as clone

#Configure Env Vars
Global_Proxy = config.Global_Proxy
if Global_Proxy == "1":
    PROXY_CREDENTIALS = env_vars.get('PROXY_CREDENTIALS')

    proxies = {
    "http": PROXY_CREDENTIALS,
    "https": PROXY_CREDENTIALS
}
else:
    proxies = {}
# Configure config
SC = config.SC
SC_DOMAIN = config.SC_DOMAIN
AW = config.AW
CB = config.CB
GS = config.GS
GHD = config.GHD
ES = config.ES
GF = config.GF
GO = config.GO
RT = config.RT
TI = config.TI
OST = config.OST
VD = config.VD
HOST = config.HOST
PORT = int(config.PORT)
if env_vars.get('PORT_ENV'):
    PORT = int(env_vars.get('PORT_ENV'))
Icon = config.Icon
Name = config.Name
app = FastAPI()
app.include_router(clone)
app.include_router(alta_router)
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)
User_Agent= "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
#Tells Where to look for static files
static = Jinja2Templates(directory="static")

MANIFEST = {
    "id": "org.stremio.mammamia",
    "version": "2.1.0",
    "behaviorHints": {"configurable": True, "configurationRequired": False},
    "catalogs": [
        {
            "type": "tv",
            "id": "tv_channels",
            "name": "MammaMia",
"extra": [
                {
                    "name": "genre",
                    "isRequired": False,
                    "options": ["Rai", "Mediaset", "Sky", "Euronews", "La7", "Warner Bros", "FIT", "Sportitalia","RSI","DAZN", "Rakuten", "Pluto", "A+E", "Paramount", "Chill"]
                }
            ]
        },
        {
            'id': 'realtime',
            'type': "series",
            "name": "realtime",
            'extra' :[
                {
                    "name": "search",
                    "isRequired": True
                }
            ]
        }
    ],
    "resources": ["stream", "catalog", "meta"],
    "types": ["movie", "series", "tv"],
    "name": Name,
    "description": "Addon providing HTTPS Streams for Italian Movies, Series, and Live TV! Note that you need to have Kitsu Addon installed in order to watch Anime",
    "logo": "https://raw.githubusercontent.com/dllfpp/MammaMia/main/static/mammamia-logo.png"
}


def respond_with(data):
    resp = JSONResponse(data)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = '*'
    return resp



@app.get('/configure',response_class=HTMLResponse)
def addon_configure(request: Request):
    forwarded_proto = request.headers.get("x-forwarded-proto")
    scheme = forwarded_proto if forwarded_proto else request.url.scheme
    instance_url = f"{scheme}://{request.url.netloc}"
    html_content = CONFIGURE.replace("{instance_url}", instance_url)
    return HTMLResponse(html_content, headers={"Cache-Control": "no-store"})
@app.get('/{config:path}/configure', response_class=HTMLResponse)
def configured_addon_configure(request: Request, config: str):
    return addon_configure(request)

@app.get('/{config:path}/manifest.json')
def addon_manifest(config: str):
    manifest_copy = deepcopy(MANIFEST)
    config = base64.b64decode(config).decode('utf-8')
    if "LIVETV" not in config:
        if "catalog" in manifest_copy["resources"]:
            for item in manifest_copy['catalogs']:
                if item['id'] == 'tv_channels':
                    manifest_copy['catalogs'].remove(item)
            if not any(manifest_copy['catalogs']):
                manifest_copy["resources"].remove('catalog')
    if 'RT' not in config or RT == '0':
        if "catalog" in manifest_copy["resources"]:
            for item in manifest_copy['catalogs']:
                if item['id'] == 'realtime':
                    manifest_copy['catalogs'].remove(item)
            if not any(manifest_copy['catalogs']):
                manifest_copy["resources"].remove('catalog')
    return respond_with(manifest_copy)

@app.get('/manifest.json')
def manifest():
    return RedirectResponse(url="/|SC|LC|/manifest.json")

@app.get('/', response_class=HTMLResponse)
def root(request: Request):
    forwarded_proto = request.headers.get("x-forwarded-proto")
    scheme = forwarded_proto if forwarded_proto else request.url.scheme
    instance_url = f"{scheme}://{request.url.netloc}"
    html_content = HTML.replace("{instance_url}", instance_url)
    return HTMLResponse(html_content, headers={"Cache-Control": "no-store"})
async def addon_catalog(type: str, id: str, genre: str = None):
    if type != "tv":
        raise HTTPException(status_code=404)

    catalogs = {"metas": []}

    for channel in STREAM["channels"]:
        if genre and genre not in channel.get("genres", []):
            continue  # Skip channels that don't match the selected genre

        description = f'Watch {channel["title"]}'
        catalogs["metas"].append({
            "id": channel["id"],
            "type": "tv",
            "name": channel["title"],
            "poster": channel["poster"],  # Add poster URL if available
            "description": description,
            "genres": channel.get("genres", [])
        })

    return catalogs
@app.get('/{config:path}/catalog/{type}/{id}.json')
@limiter.limit("5/second")
async def first_catalog(request: Request,type: str, id: str, genre: str = None):
    catalogs = await addon_catalog(type, id,genre)
    return respond_with(catalogs)

@app.get('/{config:path}/catalog/{type}/{id}/genre={genre}.json')
async def first_catalog(type: str, id: str, genre: str = None):
    catalogs = await addon_catalog(type, id,genre)
    return respond_with(catalogs)

@app.get('/{config:path}/catalog/{type}/{id}/search={query}.json')
async def realtime_catalog(type:str,id:str,query: str = None):
    if type != 'series':
        raise HTTPException(status_code=404)
    catalogs = {"query": query,'cacheMaxAge': 86400,"metas": []}
    async with AsyncSession(proxies = proxies) as client:
        catalogs = await realtime(query, catalogs,client)
    return respond_with(catalogs)
@app.get('/{config:path}/meta/tv/{id}.json')
@limiter.limit("20/second")
async def addon_meta(request: Request,id: str):
    # Find the channel by ID
    channel = next((ch for ch in STREAM['channels'] if ch['id'] == id), None)

    if not channel:
        raise HTTPException(status_code=404, detail="Channel not found")
    async with AsyncSession(proxies = proxies) as client:
        if channel["id"] in convert_bho_1 or channel["id"] in convert_bho_2 or channel["id"] in convert_bho_3:
            description,title =  await epg_guide(channel["id"],client)
        elif channel["id"] in tivu:
            description = await tivu_get(channel["id"],client)
            title = ""
        else:
            description = f'Watch {channel["title"]}'
            title = ""
    meta = {
        'meta': {
            'id': channel['id'],
            'type': 'tv',
            'name': channel['name'],
            'poster': channel['poster'],
            'posterShape': 'landscape',
            'description': title + "\n" + description,
            # Additional fields can be added here
            'background': channel['poster'],  # Example of using the same poster as background
            'logo': channel['poster'],
            'genres': channel.get('genres', []),  # Example of using the same poster as logo
        }
    }
    if 'url' in channel:
        meta['meta']['url'] = channel['url']  # Using the stream URL as a website link
    return respond_with(meta)

@app.get('/{config:path}/meta/series/{id}.json')
async def addon_meta(request: Request,id: str):
    meta = {'meta': {'videos':[], 'status': 'Continuing', 'type': 'series', 'id': id}}
    async with AsyncSession(proxies = proxies) as client:
        if 'realtime' not in id:
            raise HTTPException(status_code=404)
        meta = await meta_catalog_realtime(id,meta,client)
    return respond_with(meta)
@app.get('/{config:path}/stream/{type}/{id}.json')
@limiter.limit("5/second")
async def addon_stream(request: Request,config, type, id,):
    if type not in MANIFEST['types']:
        raise HTTPException(status_code=404)
    streams = {'streams': []}
    config = base64.b64decode(config).decode('utf-8')
    config_providers = config.replace('%7C','|').split('|')
    if 'SC' in config_providers and 'AD_OFF' not in config_providers and not any(p in config_providers for p in ('AD','VD')):
        config_providers.append('AD')
    provider_maps = {name: "0" for name in provider_map.values()}
    for provider in config_providers:
            if provider in provider_map:
                provider_name = provider_map[provider]
                provider_maps[provider_name] = "1"
    if "MFP[" in config:
    # Extract proxy data between "MFP(" and ")"
        mfp_data = config.split("MFP[")[1].split(")")[0]
    # Split the data by comma to get proxy URL and password
        MFP_url, MFP_password = mfp_data.split(",")
        MFP_password = MFP_password[:-2]
        #If mfp_url ends with a string we remove it
        if MFP_url.endswith('/'):
            MFP_url = MFP_url[:-1]
    # Store them in a list
        MFP_CREDENTIALS = [MFP_url, MFP_password]
        if MFP_url and MFP_password:
            MFP = "1"

    else:
        MFP = "0"
        MFP_CREDENTIALS = ['','']
    #Get instance URL to pass it to vidxgo
    forwarded_proto = request.headers.get("x-forwarded-proto")
    scheme = forwarded_proto if forwarded_proto else request.url.scheme
    instance_url = f"{scheme}://{request.url.netloc}"
    async with AsyncSession(proxies = proxies) as client:
        if type == "tv":
            for channel in STREAM["channels"]:
                if channel["id"] == id:
                    i = 0
                    if 'url' in channel:
                        i = i+1
                        streams['streams'].append({'title': f"{Icon}Server {i} " + f" "+ channel['name'] + " " + channel['title'] ,'url': channel['url']})
                    if id in extra_sources:
                        list_sources = extra_sources[id]
                        for item in list_sources:
                            i = i+1
                            streams['streams'].append({'title':f"{Icon}Server {i} " + channel['title'],'url': item})
            if not streams['streams']:
                raise HTTPException(status_code=404)
            for stream in streams['streams']:
                stream.setdefault('name',f'{Name} · LiveTV')
                stream.setdefault('description',stream.get('title',''))
            return respond_with_streams(streams, request, type, id)
        elif "realtime" in id and RT == '1':
            streams = await labelled_provider('Realtime', streams_realtime, streams,id,client)
            return respond_with_streams(streams, request, type, id)
        elif "tt" in id or "tmdb" in id or "kitsu" in id:
            logger.info(f"Handling movie or series: {id}")
            if "kitsu" in id:
                if provider_maps['ANIMEWORLD'] == "1" and AW == "1":
                    streams = await labelled_provider('AnimeWorld', animeworld, streams,id,client)
            else:
                if provider_maps['STREAMINGCOMMUNITY'] == "1" and SC == "1":
                    if provider_maps['SC_MFP'] != "0":
                        SC_MFP = "1"
                    else:
                        SC_MFP = '0'
                    streams = await labelled_provider('StreamingCommunity', streaming_community, streams,id,client,SC_MFP,MFP_CREDENTIALS)

                if provider_maps['CB01'] == "1" and CB == "1":
                    streams = await labelled_provider('CB01', cb01, streams,id,MFP,MFP_CREDENTIALS,client)
                if provider_maps['GUARDASERIE'] == "1" and GS == "1":
                    streams = await labelled_provider('Guardaserie', guardaserie, streams,id,client)
                if provider_maps['GUARDAHD'] == "1" and GHD == "1":
                    streams = await labelled_provider('GuardaHD', guardahd, streams,id,client,MFP,MFP_CREDENTIALS)
                if provider_maps['EUROSTREAMING'] == "1" and ES == "1":
                    streams = await labelled_provider('Eurostreaming', eurostreaming, streams,id,client,MFP,MFP_CREDENTIALS)
                if provider_maps['GUARDAFLIX'] == "1" and GF == "1":
                    streams = await labelled_provider('Guardaflix', guardaflix, streams,id,client,MFP,MFP_CREDENTIALS)
                if provider_maps['GUARDOSERIE'] == "1" and GO == "1":
                    streams = await labelled_provider('Guardoserie', guardoserie, streams,id,client,MFP,MFP_CREDENTIALS)
                if provider_maps['REALTIME'] == '1' and RT == '1':
                    streams = await labelled_provider('Realtime', streams_realtime, streams,id,client)
                if provider_maps['TOONITALIA'] == '1' and TI == '1':
                    streams = await labelled_provider('Toonitalia', toonitalia, streams,id,client,MFP,MFP_CREDENTIALS)
                if provider_maps['ONLINESERIETV'] == '1' and OST == '1':
                    streams = await labelled_provider('OnlineSerieTV', onlineserietv, streams,id,client)
                if provider_maps['VIDXGO'] == '1' and VD == '1':
                    streams = await labelled_provider('AltaDefinizione', vidxgoalta, streams,id,client,instance_url)

            return respond_with_streams(streams, request, type, id)
        if not streams['streams']:
            raise HTTPException(status_code=404)

    return respond_with_streams(streams, request, type, id)

async def labelled_provider(label, function, streams, *args):
    previous={id(stream) for stream in streams.get('streams',[])}
    streams=await function(streams,*args)
    for stream in streams.get('streams',[]):
        if id(stream) in previous:continue
        original=stream.get('name','')
        if label.lower() not in original.lower():
            suffix=original.removeprefix(Name)
            if suffix and not suffix[0].isspace():suffix='\n'+suffix
            stream['name']=f'{Name} · {label}' + suffix
        title=stream.get('title') or stream.get('description') or ''
        if label.lower() not in title.lower():title=label+'\n'+title
        stream['title']=title
        stream['description']=title
    return streams


def respond_with_streams(streams, request, type, id):
    if not request.url.path.startswith('/vlc/'):
        scheme = request.headers.get('x-forwarded-proto', request.url.scheme)
        endpoint = f"{scheme}://{request.url.netloc}/vlc/{type}/{quote(id, safe=':')}.m3u8"
        for stream in streams.get('streams', []):
            if stream.get('name', '').endswith(' TV Proxy') and stream.get('url'):
                stream['url'] = endpoint
    return respond_with(streams)

@app.get('/vlc/{type}/{id}.m3u8')
async def vlc_stream(request: Request, type: str, id: str):
    # Keep the iOS handoff URL free of nested, percent-encoded proxy queries.
    if type not in ('movie', 'series'):
        raise HTTPException(status_code=404)
    response = await addon_stream(request=request, config=base64.b64encode(b'|SC|SC_MFP|AD_OFF|').decode(), type=type, id=id)
    candidates = json.loads(response.body).get('streams', [])
    stream = next((s for s in candidates if s.get('name', '').endswith(' TV Proxy') and s.get('url')), None)
    if stream is None:
        raise HTTPException(status_code=404, detail='No TV Proxy stream available')
    async with AsyncSession() as client:
        upstream = await client.get(stream['url'], timeout=30)
    if upstream.status_code != 200 or not upstream.text.startswith('#EXTM3U'):
        raise HTTPException(status_code=502, detail='Unable to fetch HLS manifest')
    manifest = upstream.text
    if '#EXT-X-VERSION:' not in manifest:
        manifest = manifest.replace('#EXTM3U', '#EXTM3U\n#EXT-X-VERSION:6', 1)
    response = Response(content=manifest, media_type='application/vnd.apple.mpegurl')
    response.headers['Cache-Control'] = 'no-store'
    return response

@app.get('/uprot')
async def uprot(request: Request):
    async with AsyncSession(proxies = proxies) as client:
        image, cookies = await get_uprot_numbers(client)
    context = {
        'request': request,
        'image_url': image
    }

    response = static.TemplateResponse(name='uprot.html',context=context,request=request)
    if cookies:
        response.set_cookie(key='PHPSESSID', value=cookies.get('PHPSESSID'),httponly=True)

    return response
@app.post("/uprot")
async def execute_uprot(request: Request,user_input = Form(...),PHPSESSID: str = Cookie(None)):
    async with AsyncSession(proxies = proxies) as client:
        cookies = {
            'PHPSESSID': PHPSESSID
        }
        status = await generate_uprot_txt(user_input,cookies,client)
    if status == True:
        context = {
        'request': request,
        'image_url': 'https://tinyurl.com/doneokdone'
        }
        return static.TemplateResponse(name='uprot.html',context=context,request=request)
    elif status == False:
        context = {
            'request': request,
            'image_url': 'https://tinyurl.com/tryagaindumb'
        }
        return static.TemplateResponse('uprot.html',context=context,request=request)

@app.get('/update')
async def update(request: Request):
    async with AsyncSession(proxies = proxies) as client:
        result = await update_all_sites(client)
        print(result)
        if result:
            return JSONResponse(content={"message": "200"})
        if not result:
            return JSONResponse(content={"message": "Failed"})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("run:app", host=HOST, port=PORT, log_level=level)
