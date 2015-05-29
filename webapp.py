#!./env/bin/python3

from flask import Flask
from google_player import search

app = Flask(__name__)

@app.route("/")
def usage():
    return "usage : http://ip/artist/title"

@app.route("/<artist>/<title>")
def get_song(artist, title):
    return search(artist, title)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
