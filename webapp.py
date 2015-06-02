#!./env/bin/python3

from flask import Flask
from google_player import search

app = Flask(__name__)

@app.route("/")
def usage():
    return "usage : http://ip/artist/title"

@app.route("/<artist>/<title>")
def get_song(artist, title):
    result = search(artist, title)
    if result is None:
        return "Song not found :(", 404
    return '<audio controls><source src="%s"/></audio><br/>Direct link : %s' %(result, result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, threaded=True, debug=True)
