from flask import Flask, jsonify, abort
from filmpertutti import get_stream_link

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
        
    url = get_stream_link(id)  # call the function to dynamically get stream links
    

    streams = {'streams': [{'title': 'Stream URL', 'url': url}]}

    return respond_with(streams)

if __name__ == '__main__':
    app.run(locals,port=5000)
