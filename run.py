from flask import Flask, jsonify, abort
from filmpertutti import filmpertutti
from streamingcommunity import streaming_community
from tantifilm import tantifilm
import json
import config
FILMPERTUTTI = config.FILMPERTUTTI
STREAMINGCOMMUNITY = config.STREAMINGCOMMUNITY
MYSTERIUS = config.MYSTERIUS
TUTTIFILM = config.TUTTIFILM
HOST = config.HOST
PORT = int(config.PORT)
if MYSTERIUS == "1":
    from cool import cool


app = Flask(__name__)

MANIFEST = {
    "id": "org.stremio.mammamia",
    "version": "1.0.0",
    "catalogs": [],
    "resources": ["stream"],
    "types": ["movie", "series"],
    "name": "Mamma Mia",
    "description": "Addon providing HTTPS Stream for Italian Movies/Series",
    "logo":"https://creazilla-store.fra1.digitaloceanspaces.com/emojis/49647/pizza-emoji-clipart-md.png"
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



@app.route('/stream/<type>/<id>.json')
def addon_stream(type, id):
    if type not in MANIFEST['types']:
        abort(404) 
    streams = {'streams': []}
    if MYSTERIUS == "1":
        results = cool(id)
        if results:
            for resolution, link in results.items():
                streams['streams'].append({'title': f'Mysterious {resolution}', 'url': link})
    if STREAMINGCOMMUNITY == "1":
        url_streaming_community = streaming_community(id)
        print(url_streaming_community)
        if url_streaming_community is not None:
            streams['streams'].append({'title': 'StreamingCommunity 1080p', 'url': f'{url_streaming_community}?rendition=1080p'})
            streams['streams'].append({'title': 'StreamingCommunity 720p', 'url': f'{url_streaming_community}?rendition=720p'})
            
    # If FILMPERTUTTI == 1, scrape that site      
    if FILMPERTUTTI == "1":
        url_filmpertutti = filmpertutti(id)
        if url_filmpertutti is not None:
            streams['streams'].append({'title': 'Filmpertutti', 'url': url_filmpertutti})
    if TUTTIFILM == "1":
        url_tuttifilm = tantifilm(id)
        streams['streams'].append({'title': 'Tantifilm', 'url': url_tuttifilm,'behaviorHints': {'proxyHeaders': {"request": {"Referer": "https://d000d.com/"}},'notWebReady': True}})
    # If no streams were added, abort with a 404 error
    if not streams['streams']:
        abort(404)

    return respond_with(streams)


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
