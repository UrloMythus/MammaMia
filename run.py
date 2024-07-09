from flask import Flask, jsonify, abort
from filmpertutti import filmpertutti
from streamingcommunity import streaming_community
from loadenv import load_env
TMDB_KEY, FT_DOMAIN, SC_DOMAIN, FILMPERTUTTI, STREAMINGCOMMUNITY = load_env()


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
    
    # If no streams were added, abort with a 404 error
    if not streams['streams']:
        abort(404)

    return respond_with(streams)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
