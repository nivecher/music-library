from flask import Blueprint, render_template, flash, redirect, request, url_for
from app import db
from app.models.genre import GenreEnum
from app.models.song import Song
from app.models.artist import Artist
from app.models.album import Album

genres_bp = Blueprint("genres", __name__, url_prefix="/genres")


# List all genres
@genres_bp.route("/", methods=["GET"])
def index():
    return render_template("genres/index.html", genres=GenreEnum)


# Show details of a specific genre
@genres_bp.route("/<string:genre_name>", methods=["GET"])
def show(genre_name):
    genre = GenreEnum.get_genre_enum(genre_name)
    if genre is None:
        flash("Genre not found", "danger")
        return redirect(url_for("genres.index"))

    # Fetch the songs and albums for the artist and sort them by title
    songs = db.session.query(Song).filter_by(genre=genre).order_by(Song.title).all()
    albums = db.session.query(Album).filter_by(genre=genre).order_by(Album.title).all()
    # TODO artists = db.session.query(Artist).filter_by(genre=genre).order_by(Artist.name).all()

    return render_template("genres/show.html", genre_name=genre_name, genre_songs=songs, genre_albums=albums)
