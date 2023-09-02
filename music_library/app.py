from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_debugtoolbar import DebugToolbarExtension  # Import the DebugToolbarExtension
import json

app = Flask(__name__)

# Enable Flask Debug Toolbar
app.config[
    "SECRET_KEY"
] = "d1c3b3f066f6dff7de23d1035f34b3ce3198d9022d957b7911a2931d60974ff8"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
toolbar = DebugToolbarExtension(app)

# Load initial song data from a JSON file
with open("data/songs.json", "r") as json_file:
    songs = json.load(json_file)

# Define routes


@app.route("/")
def index():
    sorted_songs = sorted(songs, key=lambda x: x["title"])
    return render_template("index.html", songs=sorted_songs)


@app.route("/add_song", methods=["GET", "POST"])
def add_song():
    if request.method == "POST":
        new_song = {
            "title": request.form.get("title"),
            "artist": request.form.get("artist"),
            "album": request.form.get("album"),
            "genre": request.form.get("genre"),
        }
        songs.append(new_song)
        with open("data/songs.json", "w") as json_file:
            json.dump(songs, json_file, indent=4)
        return redirect(url_for("index"))
    return render_template("add_song.html")


@app.route("/song/<int:song_id>")
def song_details(song_id):
    song = songs[song_id]
    return render_template("song_details.html", song=song)


@app.route("/artist/<string:artist_name>")
def artist_details(artist_name):
    artist_songs = [song for song in songs if song["artist"] == artist_name]
    return render_template(
        "artist_details.html", artist_name=artist_name, artist_songs=artist_songs
    )


@app.route("/genre/<string:genre_name>")
def genre_details(genre_name):
    genre_songs = [song for song in songs if song["genre"] == genre_name]
    return render_template(
        "genre_details.html", genre_name=genre_name, genre_songs=genre_songs
    )


@app.route("/api/songs", methods=["GET"])
def get_songs():
    return jsonify(songs)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)  # Enable the reloader
