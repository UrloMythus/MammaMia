from flask import Flask, jsonify, abort
from filmpertutti import filmpertutti
from streamingcommunity import streaming_community
from tantifilm import tantifilm
import json
import config
import logging

# Configure logging

FILMPERTUTTI = config.FILMPERTUTTI
STREAMINGCOMMUNITY = config.STREAMINGCOMMUNITY
MYSTERIUS = config.MYSTERIUS
TUTTIFILM = config.TUTTIFILM
TF_DOMAIN = config.TF_DOMAIN
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

app = Flask(__name__)

MANIFEST = {
    "id": "org.stremio.mammamia",
    "version": "1.0.0",
    "catalogs": [
        {"type": "tv", "id": "tv_channels", "name": "TV Channels"}
    ],
    "resources": ["stream", "catalog","meta"],
    "types": ["movie", "series", "tv"],
    "name": "Mamma Mia",
    "description": "Addon providing HTTPS Stream for Italian Movies/Series",
    "logo": "https://creazilla-store.fra1.digitaloceanspaces.com/emojis/49647/pizza-emoji-clipart-md.png"
}

STREAMS = {
    "tv": {
        "skysport24": [
            {
                "title": "Sky Sport 24",
                "poster": f"https://www.tanti.{TF_DOMAIN}/public/upload/channel/sky-sport-24.webp",
                "url": "https://07-24.mizhls.ru/fls/cdn/calcioXskysport24/playlist.m3u8",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "Referer": "https://claplivehdplay.ru/",
                            "Origin": "https://claplivehdplay.ru",
                            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
                        }
                    }
                }
            }
        ],
        "Skyuno": [
            {
                "title": "Sky Uno",
                "poster": f"https://www.tanti.{TF_DOMAIN}/public/upload/channel/sky-uno.webp",
                "url": "https://07-24.mizhls.ru/fls/cdn/calcioXskyuno/playlist.m3u8",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "Referer": "https://claplivehdplay.ru/",
                            "Origin": "https://claplivehdplay.ru",
                            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
                        }
                    }
                }
            }
        ],
        "skyserie": [
            {
                "title": "Sky Serie",
                "poster": f"https://www.tanti.{TF_DOMAIN}/public/upload/channel/sky-serie.webp",
                "url": "https://07-24.mizhls.ru/fls/cdn/calcioXskyserie/playlist.m3u8",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "Referer": "https://claplivehdplay.ru/",
                            "Origin": "https://claplivehdplay.ru",
                            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
                        }
                    }
                }
            }
        ],
        "Sky Nature": [
            {
                "title": "Sky Nature",
                "poster": f"https://www.tanti.{TF_DOMAIN}/public/upload/channel/sky-nature.webp",
                "url": "https://07-24.mizhls.ru/fls/cdn/calcioXskynature/playlist.m3u8",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "Referer": "https://claplivehdplay.ru/",
                            "Origin": "https://claplivehdplay.ru",
                            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
                        }
                    }
                }
            }
        ],
        "skyinvestigation": [
            {
                "title": "skyinvestigation",
                "poster": f"https://www.tanti.{TF_DOMAIN}/public/upload/channel/sky-nature.webp",
                "url": "https://07-24.mizhls.ru/fls/cdn/calcioXskyinvestigation/playlist.m3u8",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "Referer": "https://claplivehdplay.ru/",
                            "Origin": "https://claplivehdplay.ru",
                            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
                        }
                    }
                }
            }
        ]
    }
}

def respond_with(data):
    resp = jsonify(data)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = '*'
    return resp

@app.route('/manifest.json')
def addon_manifest():
    return respond_with(MANIFEST)

@app.route('/')
def root():
    return "Hello, this is a Stremio Addon providing HTTPS Stream for Italian Movies/Series, to install it add /manifest.json to the url and then add it into the Stremio search bar"

@app.route('/catalog/<type>/<id>.json')
def addon_catalog(type, id):
    if type not in MANIFEST['types']:
        abort(404)
    catalog = {'metas': []}
    if type in STREAMS:
        for stream_id in STREAMS[type]:
            for item in STREAMS[type][stream_id]:
                meta_item = {
                    "id": stream_id,
                    "type": type,
                    "name": item['title'],
                    "poster": item.get('poster', "https://via.placeholder.com/150")
                }
                catalog['metas'].append(meta_item)
    return respond_with(catalog)

@app.route('/stream/<type>/<id>.json')
def addon_stream(type, id):
    if type not in MANIFEST['types']:
        abort(404)
    streams = {'streams': []}

    if type in STREAMS and id in STREAMS[type]:
        logging.debug(f"Found TV channel: {id}")
        streams['streams'] = STREAMS[type][id]
    else:
        logging.debug(f"Handling movie or series: {id}")
        if MYSTERIUS == "1":
            results = cool(id)
            if results:
                for resolution, link in results.items():
                    streams['streams'].append({'title': f'{HF}Mysterious {resolution}', 'url': link})
        if STREAMINGCOMMUNITY == "1":
            url_streaming_community = streaming_community(id)
            if url_streaming_community is not None:
                streams['streams'].append({'title': f'{HF}StreamingCommunity 1080p', 'url': f'{url_streaming_community}?rendition=1080p'})
                streams['streams'].append({'title': f'{HF}StreamingCommunity 720p', 'url': f'{url_streaming_community}?rendition=720p'})
        if FILMPERTUTTI == "1":
            url_filmpertutti = filmpertutti(id)
            if url_filmpertutti is not None:
                streams['streams'].append({'title': 'Filmpertutti', 'url': url_filmpertutti})
        if TUTTIFILM == "1":
            try:
                url_tuttifilm = tantifilm(id)
                if not isinstance(url_tuttifilm, str):
                    for title, url in url_tuttifilm.items():    
                        streams['streams'].append({'title': f'{HF}Tantifilm {title}', 'url': url,  'behaviorHints': {'proxyHeaders': {"request": {"Referer": "https://d000d.com/"}}, 'notWebReady': True}})
                else:
                    streams['streams'].append({'title': f'{HF}Tantifilm', 'url': url_tuttifilm, 'behaviorHints': {'proxyHeaders': {"request": {"Referer": "https://d000d.com/"}}, 'notWebReady': True}})
            except Exception as e:
                print("Tantifilm error")
    if not streams['streams']:
        abort(404)

    return respond_with(streams)

@app.route('/meta/<type>/<id>.json')
def meta(type, id):
    if type not in MANIFEST['types']:
        abort(404)

    meta = {}
    for stream_id in STREAMS.get(type, {}):
        if stream_id == id:
            item = STREAMS[type][stream_id][0]  # Assuming there's at least one item
            meta = {
                "id": stream_id,
                "type": type,
                "name": item['title'],
                "poster": item.get('poster', "https://icons.iconarchive.com/icons/designbolts/free-multimedia/256/TV-icon.png"),
                "background": item.get('background', "https://icons.iconarchive.com/icons/designbolts/free-multimedia/256/TV-icon.png")
            }
            break

    if not meta:
        abort(404)

    return respond_with({"meta": meta})
if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
