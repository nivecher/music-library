from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

app = Flask(__name__)

# Load initial song data from a JSON file
with open("data/songs.json", "r") as json_file:
    songs = json.load(json_file)

# Define routes


@app.route("/")
def index():
    # TODO add current_year, etc. to enrich base
    return render_template("index.html", songs=songs)


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


@app.route("/album/<string:album_name>")
def album_details(album_name):
    album_songs = [song for song in songs if song["album"] == album_name]
    return render_template(
        "album_details.html", album_name=album_name, album_songs=album_songs
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
    app.run(debug=True)
