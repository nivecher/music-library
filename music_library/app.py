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


@app.route("/artists")
def artists():
    # Extract a list of unique artist names
    artist_names = list(set(song["artist"] for song in songs))
    sorted_artist_names = sorted(artist_names)
    return render_template("artists.html", artist_names=sorted_artist_names)


@app.route("/artist/<string:artist_name>")
def artist_details(artist_name):
    artist_songs = [song for song in songs if song["artist"] == artist_name]

    # Extract a list of unique album names associated with the artist
    artist_albums = list(set(song["album"] for song in artist_songs))

    return render_template(
        "artist_details.html",
        artist_name=artist_name,
        artist_songs=artist_songs,
        artist_albums=artist_albums,  # Pass the list of albums
    )


@app.route("/albums")
def albums():
    # Extract a list of unique album names
    album_names = list(set(song["album"] for song in songs))
    sorted_album_names = sorted(album_names)
    return render_template("albums.html", album_names=sorted_album_names)


@app.route("/album/<string:album_name>")
def album_details(album_name):
    album_songs = [song for song in songs if song["album"] == album_name]
    return render_template(
        "album_details.html", album_name=album_name, album_songs=album_songs
    )


@app.route("/genres")
def genres():
    # Extract a list of unique genre names
    genre_names = list(set(song["genre"] for song in songs))
    sorted_genre_names = sorted(genre_names)
    return render_template("genres.html", genre_names=sorted_genre_names)


@app.route("/genre/<string:genre_name>")
def genre_details(genre_name):
    genre_songs = [song for song in songs if song["genre"] == genre_name]

    # Sort the songs by title (alphabetically)
    sorted_genre_songs = sorted(genre_songs, key=lambda song: song["title"])

    # Extract a list of unique album names associated with the genre
    genre_albums = list(set(song["album"] for song in sorted_genre_songs))

    # TODO sort albums by year

    # Sort the albums by title (alphabetically)
    sorted_genre_albums = sorted(genre_albums)

    return render_template(
        "genre_details.html",
        genre_name=genre_name,
        genre_songs=sorted_genre_songs,
        genre_albums=sorted_genre_albums,
    )


@app.route("/api/songs", methods=["GET"])
def get_songs():
    return jsonify(songs)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)  # Enable the reloader
