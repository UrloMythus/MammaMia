from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from filmpertutti import filmpertutti
from streamingcommunity import streaming_community
from tantifilm import tantifilm
from lordchannel import lordchannel
from streamingwatch import streamingwatch
import json
import config
import logging
from okru import okru_get_url
from animeworld import animeworld
from dictionaries import okru,STREAM
import httpx
# Configure logging
FILMPERTUTTI = config.FILMPERTUTTI
STREAMINGCOMMUNITY = config.STREAMINGCOMMUNITY
MYSTERIUS = config.MYSTERIUS
TUTTIFILM = config.TUTTIFILM
TF_DOMAIN = config.TF_DOMAIN
LORDCHANNEL = config.LORDCHANNEL
STREAMINGWATCH= config.STREAMINGWATCH
ANIMEWORLD = config.ANIMEWORLD
HOST = config.HOST
PORT = int(config.PORT)
HF = config.HF
if HF == "1":
    HF = "🤗️"
    #Cool code to set the hugging face if the service is hosted there.
else:
    HF = ""
if MYSTERIUS == "1":
    from cool import cool

app = FastAPI()
MANIFEST = {
    "id": "org.stremio.mammamia",
    "version": "1.0.5",
    "catalogs": [
        {"type": "tv", "id": "tv_channels", "name": "TV Channels"}
    ],
    "resources": ["stream", "catalog","meta"],
    "types": ["movie", "series", "tv"],
    "name": "Mamma Mia",
    "description": "Addon providing HTTPS Streams for Italian Movies,Series and Live TV! Note that you need to have Kitsu Addon installed in order to watch Anime",
    "logo": "https://creazilla-store.fra1.digitaloceanspaces.com/emojis/49647/pizza-emoji-clipart-md.png"
}



def respond_with(data):
    resp = JSONResponse(data)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = '*'
    return resp

@app.get('/manifest.json')
def addon_manifest():
    return respond_with(MANIFEST)

@app.get('/')
def root():
    return "Hello, this is a Stremio Addon providing HTTPS Stream for Italian Movies/Series, to install it add /manifest.json to the url and then add it into the Stremio search bar"

@app.get('/catalog/{type}/{id}.json')
def addon_catalog(type, id):
    print("STA ANDANDO TUTTO MALE")
    if type != "tv":
        raise HTTPException(status_code=404)

    catalogs = {"metas": []}
    for channel in STREAM["channels"]:
        catalogs["metas"].append({
            "id": channel["id"],
            "type": "tv",
            "name": channel["title"],
            "poster": channel["poster"],  # Add poster URL if available
            "description": f"Watch {channel['title']}"
        })

    return respond_with(catalogs)

@app.get('/meta/{type}/{id}.json')
def addon_meta(type, id):
    if type != "tv":
        raise HTTPException(status_code=404)

    for channel in STREAM["channels"]:
        if channel["id"] == id:
            meta = {
                "id": id,
                "type": "tv",
                "name": channel["title"],
                "poster": channel["poster"],  # Add poster URL if available
                "description": f"Watch {channel['title']}",
                "background": "",  # Add background image URL if available
                "logo": "",  # Add logo URL if available
                "videos": [{
                    "title": channel["title"],
                    "streams": [{
                        "title": channel["title"],
                        "url": channel["url"]
                    }]
                }]
            }
            return respond_with({"meta": meta})

    raise HTTPException(status_code=404)


@app.get('/stream/{type}/{id}.json')
async def addon_stream(type, id):
    if type not in MANIFEST['types']:
        raise HTTPException(status_code=404)
    streams = {'streams': []}
    async with httpx.AsyncClient() as client:
        if type == "tv":
            for channel in STREAM["channels"]:
                if channel["id"] == id:
                    streams['streams'].append({
                        'title': channel['name'],
                        'url': channel['url']
                        })
                    if id in okru:
                        channel_url = await okru_get_url(id,client)
                        streams['streams'].append({
                            'title': channel['name'] + "OKRU",
                            'url': channel_url
                        })
            if not streams['streams']:
                raise HTTPException(status_code=404)
            return respond_with(streams)
        else:
            logging.debug(f"Handling movie or series: {id}")
            if "kitsu" in id:
                if ANIMEWORLD == "1":
                    animeworld_urls = await animeworld(id,client)
                    print(animeworld_urls)
                    if animeworld_urls:
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
                        for resolution, link in results.items():
                            streams['streams'].append({'title': f'{HF}Mysterious {resolution}', 'url': link})
                if STREAMINGCOMMUNITY == "1":
                    url_streaming_community,url_720_streaming_community,quality_sc = await streaming_community(id,client)
                    if url_streaming_community is not None:
                        if quality_sc == "1080":
                            streams['streams'].append({'title': f'{HF}StreamingCommunity 1080p Max', 'url': url_streaming_community})
                            streams['streams'].append({'title': f'{HF}StreamingCommunity 720p Max', 'url': url_720_streaming_community})
                        else:
                            streams['streams'].append({'title': f'{HF}StreamingCommunity 720p Max', 'url': url_streaming_community})
                if LORDCHANNEL == "1":
                    url_lordchannel,quality_lordchannel = await lordchannel(id,client)
                    if quality_lordchannel == "FULL HD" and url_lordchannel !=  None:
                        streams['streams'].append({'title': f'{HF}LordChannel 1080p', 'url': url_lordchannel})
                    elif url_lordchannel !=  None:
                        streams['streams'].append({'title': f'{HF}LordChannel 720p', 'url': url_lordchannel})            
                if FILMPERTUTTI == "1":
                    url_filmpertutti = await filmpertutti(id,client)
                    if url_filmpertutti is not None:
                        streams['streams'].append({'title': 'Filmpertutti', 'url': url_filmpertutti})
                if TUTTIFILM == "1":
                    url_tuttifilm = await tantifilm(id,client)
                    if url_tuttifilm:
                        if not isinstance(url_tuttifilm, str):
                            for title, url in url_tuttifilm.items():    
                                streams['streams'].append({'title': f'{HF}Tantifilm {title}', 'url': url,  'behaviorHints': {'proxyHeaders': {"request": {"Referer": "https://d000d.com/"}}, 'notWebReady': True}})
                if STREAMINGWATCH == "1":
                    url_streamingwatch = await streamingwatch(id,client)
                    if url_streamingwatch:
                        streams['streams'].append({'title': f'{HF}StreamingWatch 720p', 'url': url_streamingwatch})
        if not streams['streams']:
            raise HTTPException(status_code=404)

    return respond_with(streams)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("run:app", host=HOST, port=PORT, log_level="info")