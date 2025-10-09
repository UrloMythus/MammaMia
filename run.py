from fastapi import FastAPI, HTTPException,Request
from fastapi.responses import JSONResponse,RedirectResponse,HTMLResponse
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from static.static import HTML
from static.configure import  CONFIGURE


from  Src.API.streamingcommunity import streaming_community
from  Src.API.streamingwatch import streamingwatch
from Src.API.cb01 import cb01
from Src.API.guardaserie import guardaserie
from Src.API.guardahd import guardahd
from Src.API.animeworld import animeworld
from Src.API.guardaflix import guardaflix
from Src.API.guardoserie import guardoserie
from Src.API.eurostreaming import eurostreaming

from Src.Utilities.dictionaries import STREAM,extra_sources,provider_map
from Src.API.epg import tivu, tivu_get,epg_guide,convert_bho_1,convert_bho_2,convert_bho_3

import logging
from urllib.parse import unquote
from curl_cffi.requests import AsyncSession
import base64
import  Src.Utilities.config as config
from Src.Utilities.config import setup_logging
level = config.LEVEL
logger = setup_logging(level)
from Src.Utilities.loadenv import load_env
env_vars = load_env()

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
SW = config.SW
AW = config.AW
CB = config.CB
GS = config.GS
GHD = config.GHD
ES = config.ES
GF = config.GF
GO = config.GO
HOST = config.HOST
PORT = int(config.PORT)
if env_vars.get('PORT_ENV'):
    PORT = int(env_vars.get('PORT_ENV'))
Icon = config.Icon
Name = config.Name
    #Cool code to set the hugging face if the service is hosted there.
app = FastAPI()
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)
User_Agent= "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
MANIFEST = {
    "id": "org.stremio.mammamia",
    "version": "2.0.0",
    "catalogs": [
        {
            "type": "tv",
            "id": "tv_channels",
            "name": "MammaMia",
            "behaviorHints": {
                "configurable": True,
                "configurationRequired": True
                },
            "extra": [
                {
                    "name": "genre",
                    "isRequired": False,
                    "options": ["Rai", "Mediaset", "Sky", "Euronews", "La7", "Warner Bros", "FIT", "Sportitalia","RSI","DAZN", "Rakuten", "Pluto", "A+E", "Paramount", "Chill"]
                }
            ]
        }
    ],
    "resources": ["stream", "catalog", "meta"],
    "types": ["movie", "series", "tv"],
    "name": Name,
    "description": "Addon providing HTTPS Streams for Italian Movies, Series, and Live TV! Note that you need to have Kitsu Addon installed in order to watch Anime",
    "logo": "https://creazilla-store.fra1.digitaloceanspaces.com/emojis/49647/pizza-emoji-clipart-md.png"
}


def respond_with(data):
    resp = JSONResponse(data)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = '*'
    return resp



@app.get('/configure',response_class=HTMLResponse)
def config(request: Request):
    forwarded_proto = request.headers.get("x-forwarded-proto")
    scheme = forwarded_proto if forwarded_proto else request.url.scheme
    instance_url = f"{scheme}://{request.url.netloc}"
    html_content = CONFIGURE.replace("{instance_url}", instance_url)
    return html_content
@app.get('/{config:path}/manifest.json')
def addon_manifest(config: str): 
    manifest_copy = MANIFEST.copy() 
    config = base64.b64decode(config).decode('utf-8')
    if "LIVETV"  in config:
        return respond_with(manifest_copy)
    elif "LIVETV" not in config:
        manifest_copy["catalogs"] = []
        if "catalog" in manifest_copy["resources"]:
            manifest_copy["resources"].remove("catalog")
        return respond_with(manifest_copy)

@app.get('/manifest.json')
def manifest():
    return RedirectResponse(url="/|SC|LC|SW|/manifest.json")

@app.get('/', response_class=HTMLResponse)
def root(request: Request):
    forwarded_proto = request.headers.get("x-forwarded-proto")
    scheme = forwarded_proto if forwarded_proto else request.url.scheme
    instance_url = f"{scheme}://{request.url.netloc}"
    html_content = HTML.replace("{instance_url}", instance_url)
    return html_content
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


@app.get('/{config:path}/stream/{type}/{id}.json')
@limiter.limit("5/second")
async def addon_stream(request: Request,config, type, id,):
    if type not in MANIFEST['types']:
        raise HTTPException(status_code=404)
    streams = {'streams': []}
    config = base64.b64decode(config).decode('utf-8')
    if "|" in config:
        config_providers = config.split('|')
    elif "%7C" in config:
        config_providers = config.split('%7C')
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
            return respond_with(streams)
        elif "tt" in id or "tmdb" in id or "kitsu" in id:
            logger.info(f"Handling movie or series: {id}")
            if "kitsu" in id:
                if provider_maps['ANIMEWORLD'] == "1" and AW == "1":
                    streams = await animeworld(streams,id,client)
            else:
                if provider_maps['STREAMINGCOMMUNITY'] == "1" and SC == "1":
                    if provider_maps['SC_MFP'] != "0":
                        SC_MFP = "1"
                    streams = await streaming_community(streams,id,client,SC_MFP,MFP_CREDENTIALS)
                if provider_maps['STREAMINGWATCH'] == "1" and SW == "1":
                    streams = await streamingwatch(streams,id,client)
                if provider_maps['CB01'] == "1" and CB == "1":
                    streams = await cb01(streams,id,MFP,MFP_CREDENTIALS,client)
                if provider_maps['GUARDASERIE'] == "1" and GS == "1":
                    streams = await guardaserie(streams,id,client)
                if provider_maps['GUARDAHD'] == "1" and GHD == "1":
                    streams = await guardahd(streams,id,client)
                if provider_maps['EUROSTREAMING'] == "1" and ES == "1":
                    streams = await eurostreaming(streams,id,client,MFP,MFP_CREDENTIALS)
                if provider_maps['GUARDAFLIX'] == "1" and GF == "1":
                    streams = await guardaflix(streams,id,client,MFP,MFP_CREDENTIALS)
                if provider_maps['GUARDOSERIE'] == "1" and GO == "1":
                    streams = await guardoserie(streams,id,client,MFP,MFP_CREDENTIALS)
        if not streams['streams']:
            raise HTTPException(status_code=404)

    return respond_with(streams)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("run:app", host=HOST, port=PORT, log_level=level)    
