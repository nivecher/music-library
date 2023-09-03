from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models.song import Song
from app.models.artist import Artist
from app.models.album import Album
from app.models.genre import GenreEnum


songs_bp = Blueprint("songs", __name__, url_prefix="/songs")


# List all songs (Read - R in CRUD)
@songs_bp.route("/", methods=["GET"])
def index():
    songs = db.session.query(Song).order_by(Song.title).all()
    return render_template("songs/index.html", songs=songs)


# Show details of a specific song (Read - R in CRUD)
@songs_bp.route("/<int:id>", methods=["GET"])
def show(id):
    song = Song.query.get(id)
    if song is None:
        flash("Song not found", "danger")
        return redirect(url_for("songs.index"))

    return render_template("songs/show.html", song=song)


# Show a form to create a new song (Create - C in CRUD)
@songs_bp.route("/create", methods=["GET"])
def create():
    albums = db.session.query(Album).order_by(Album.title).all()
    return render_template("songs/create.html", albums=albums, genres=GenreEnum)


# Create a new song (Create - C in CRUD)
@songs_bp.route("/", methods=["POST"])
def create_song():
    title = request.form["title"]
    artist_name = request.form["artist"]
    album_title = request.form["album"]
    genre_name = request.form["genre"]
    genre = GenreEnum.get_genre_enum(genre_name)

    # Check if the artist exists, or create it if it doesn't
    artist = Artist.query.filter_by(name=artist_name).first()
    if artist is None:
        # Artist doesn't exist, create it
        artist = Artist(name=artist_name, genre=genre)
        db.session.add(artist)
        db.session.commit()
        print(f"Created new artist: {artist}")

    # Check if the album exists, or create it if it doesn't
    album = Album.query.filter_by(title=album_title, artist_id=artist.id).first()
    if album is None:
        # Album doesn't exist, create it
        album = Album(title=album_title, artist_id=artist.id, genre=genre)
        db.session.add(album)
        db.session.commit()
        print(f"Created new album: {album}")

    new_song = Song(
        title=title,
        artist_id=artist.id,
        album_id=album.id,
        genre=genre,
    )
    db.session.add(new_song)
    db.session.commit()
    print(f"Created new song: {new_song}")

    flash("Song added successfully!", "success")
    return redirect(url_for("songs.index"))


# Show a form to edit an existing song (Update - U in CRUD)
@songs_bp.route("/<int:id>/edit", methods=["GET"])
def edit(id):
    song = Song.query.get(id)
    artists = db.session.query(Artist).order_by(Artist.name).all()
    albums = db.session.query(Album).order_by(Album.title).all()
    if song is None:
        flash("Song not found", "danger")
        return redirect(url_for("songs.index"))

    return render_template(
        "songs/edit.html",
        song=song,
        artists=artists,
        albums=albums,
        genres=GenreEnum.list(),
    )


# Show a form to updating an existing song (Update - U in CRUD)
@songs_bp.route("/<int:id>/edit", methods=["POST"])
def update_song(id):
    # Retrieve the song by its ID
    song = Song.query.get_or_404(id)

    # Get form data
    title = request.form.get("title")
    artist_id = int(request.form.get("artist_id"))
    album_id = int(request.form.get("album_id"))
    genre = request.form.get("genre")
    duration = request.form.get("duration")

    # Update song details
    song.title = title
    song.artist_id = artist_id
    song.album_id = album_id
    song.genre = genre
    song.duration = duration

    # Commit changes to the database
    db.session.commit()

    flash("Song updated successfully", "success")
    return redirect(url_for("songs.index"))


@songs_bp.route("/<int:id>/delete", methods=["DELETE"])
def delete(id):
    song = Song.query.get(id)

    if song:
        db.session.delete(song)
        db.session.commit()
        flash("Song deleted successfully!", "success")
    else:
        flash("Song not found!", "danger")

    return redirect(url_for("songs.index"))
