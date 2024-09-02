from fastapi import FastAPI, HTTPException,Request
from fastapi.responses import JSONResponse,RedirectResponse,HTMLResponse
from Src.API.filmpertutti import filmpertutti
from  Src.API.streamingcommunity import streaming_community
from  Src.API.tantifilm import tantifilm
from  Src.API.lordchannel import lordchannel
from  Src.API.streamingwatch import streamingwatch
import  Src.Utilities.config as config
import logging
from Src.API.okru import okru_get_url
from Src.API.animeworld import animeworld
from Src.Utilities.dictionaries import okru,STREAM,extra_sources,webru_vary,webru_dlhd,provider_map
from Src.API.epg import tivu, tivu_get,epg_guide,convert_bho_1,convert_bho_2,convert_bho_3
from Src.API.webru import webru
from curl_cffi.requests import AsyncSession
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from static.static import HTML
# Configure logging
MYSTERIUS = config.MYSTERIUS
HOST = config.HOST
PORT = int(config.PORT)
HF = config.HF
if HF == "1":
    HF = "🤗️"
    #Cool code to set the hugging face if the service is hosted there.
else:
    HF = ""
if MYSTERIUS == "1":
    from Src.API.cool import cool

app = FastAPI()
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)
MANIFEST = {
    "id": "org.stremio.mammamia",
    "version": "1.1.0",
    "catalogs": [
        {
            "type": "tv",
            "id": "tv_channels",
            "name": "TV Channels",
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
    "name": "Mamma Mia",
    "description": "Addon providing HTTPS Streams for Italian Movies, Series, and Live TV! Note that you need to have Kitsu Addon installed in order to watch Anime",
    "logo": "https://creazilla-store.fra1.digitaloceanspaces.com/emojis/49647/pizza-emoji-clipart-md.png"
}


def respond_with(data):
    resp = JSONResponse(data)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = '*'
    return resp

@app.get('/config')
def config():
    return RedirectResponse(url="/")
@app.get('/{config}/manifest.json')
def addon_manifest():
    return respond_with(MANIFEST)

@app.get('/', response_class=HTMLResponse)
def root(request: Request):
    instance_url = f"{request.url.scheme}://{request.url.netloc}"
    html_content = HTML.replace("{instance_url}", instance_url)
    return html_content
async def addon_catalog(type: str, id: str, genre: str = None):
    print(f"Received genre parameter: {genre}")
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
@app.get('/{config}/catalog/{type}/{id}.json')
@limiter.limit("5/second")
async def first_catalog(request: Request,type: str, id: str, genre: str = None):
    catalogs = await addon_catalog(type, id,genre)
    return respond_with(catalogs)

@app.get('/{config}/catalog/{type}/{id}/genre={genre}.json')
async def first_catalog(type: str, id: str, genre: str = None):
    catalogs = await addon_catalog(type, id,genre)
    return respond_with(catalogs)

@app.get('/{config}/meta/tv/{id}.json')
@limiter.limit("20/second")
async def addon_meta(request: Request,id: str):
    # Find the channel by ID
    channel = next((ch for ch in STREAM['channels'] if ch['id'] == id), None)
    
    if not channel:
        raise HTTPException(status_code=404, detail="Channel not found")
    async with AsyncSession() as client:
        if channel["id"] in convert_bho_1 or channel["id"] in convert_bho_2 or channel["id"] in convert_bho_3:
            description,title =  await epg_guide(channel["id"],client)
        elif channel["id"] in tivu:
            description = await tivu_get(channel["id"],client)
            print(description)
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


@app.get('/{config}/stream/{type}/{id}.json')
@limiter.limit("5/second")
async def addon_stream(request: Request,config, type, id,):
    if type not in MANIFEST['types']:
        raise HTTPException(status_code=404)
    streams = {'streams': []}
    config_providers = config.split('|')
    provider_maps = {name: "0" for name in provider_map.values()}
    for provider in config_providers:
            if provider in provider_map:
                provider_name = provider_map[provider]
                provider_maps[provider_name] = "1"

    async with AsyncSession() as client:
        if type == "tv":
            for channel in STREAM["channels"]:
                if channel["id"] == id:
                    i = 0
                    if 'url' in channel:
                        i = i+1
                        streams['streams'].append({
                            'title': f"Server {i} " + f" "+ channel['name'] + " " + channel['title'] ,
                            'url': channel['url']
                            })
                    if id in okru:
                        i = i+1
                        channel_url = await okru_get_url(id,client)
                        streams['streams'].append({
                            'title':  f"Server {i} " +  channel['title'] + " OKRU",
                            'url': channel_url
                        })
                    if id in extra_sources:
                        list_sources = extra_sources[id]
                        for item in list_sources:
                            i = i+1
                            streams['streams'].append({'title':f"Server {i} " + channel['title'],'url': item})
                    if id in webru_vary:
                        i = i+1
                        webru_url = await webru(id,"vary",client)
                        streams['streams'].append({'title': f"Server {i} " + channel['title'],'url': webru_url})
            if not streams['streams']:
                raise HTTPException(status_code=404)
            return respond_with(streams)
        else:
            logging.debug(f"Handling movie or series: {id}")
            if "kitsu" in id:
                if provider_maps['ANIMEWORLD'] == "1":
                    animeworld_urls = await animeworld(id,client)
                    if animeworld_urls:
                        print(f"AnimeWorld Found Results for {id}")
                        i = 0
                        for url in animeworld_urls:
                            if url:
                                if i == 0:
                                    title = "Original"
                                elif i == 1:
                                     title = "Italian"
                                streams['streams'].append({'title': f'{HF}Animeworld {title}', 'url': url})
                                i+=1
            else:
                if MYSTERIUS == "1":
                    results = await cool(id,client)
                    if results:
                        print(f"Mysterius Found Results for {id}")
                        for resolution, link in results.items():
                            streams['streams'].append({'title': f'{HF}Mysterious {resolution}', 'url': link})
                if provider_maps['STREAMINGCOMMUNITY'] == "1":
                    SC_FAST_SEARCH = provider_maps['SC_FAST_SEARCH']
                    url_streaming_community,url_720_streaming_community,quality_sc = await streaming_community(id,client,SC_FAST_SEARCH)
                    if url_streaming_community is not None:
                        print(f"StreamingCommunity Found Results for {id}")
                        if quality_sc == "1080":
                            streams['streams'].append({'title': f'{HF}StreamingCommunity 1080p Max', 'url': url_streaming_community})
                            streams['streams'].append({'title': f'{HF}StreamingCommunity 720p Max', 'url': url_720_streaming_community})
                        else:
                            streams['streams'].append({'title': f'{HF}StreamingCommunity 720p Max', 'url': url_streaming_community})
                if provider_maps['LORDCHANNEL'] == "1":
                    url_lordchannel,quality_lordchannel = await lordchannel(id,client)
                    if quality_lordchannel == "FULL HD" and url_lordchannel !=  None:
                        print(f"LordChannel Found Results for {id}")
                        streams['streams'].append({'title': f'{HF}LordChannel 1080p', 'url': url_lordchannel})
                    elif url_lordchannel !=  None:
                        print(f"LordChannel Found Results for {id}")
                        streams['streams'].append({'title': f'{HF}LordChannel 720p', 'url': url_lordchannel})            
                if provider_maps['FILMPERTUTTI'] == "1":
                    url_filmpertutti = await filmpertutti(id,client)
                    if url_filmpertutti is not None:
                        streams['streams'].append({'title': 'Filmpertutti', 'url': url_filmpertutti})
                if provider_maps['TANTIFILM'] == "1":
                    TF_FAST_SEARCH = provider_maps['TF_FAST_SEARCH']                    
                    url_tantifilm = await tantifilm(id,client,TF_FAST_SEARCH)
                    if url_tantifilm:
                        print(f"TantiFilm Found Results for {id}")
                        if not isinstance(url_tantifilm, str):
                            for title, url in url_tantifilm.items():    
                                streams['streams'].append({'title': f'{HF}Tantifilm {title}', 'url': url,  'behaviorHints': {'proxyHeaders': {"request": {"Referer": "https://d000d.com/"}}, 'notWebReady': True}})
                if provider_maps['STREAMINGWATCH'] == "1":
                    url_streamingwatch = await streamingwatch(id,client)
                    if url_streamingwatch:
                        streams['streams'].append({'title': f'{HF}StreamingWatch 720p', 'url': url_streamingwatch})
        if not streams['streams']:
            raise HTTPException(status_code=404)

    return respond_with(streams)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("run:app", host=HOST, port=PORT, log_level="info")