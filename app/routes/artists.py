from flask import Blueprint, render_template, flash, redirect, url_for, request
from app import db
from app.models.artist import Artist
from app.models.song import Song
from app.models.album import Album

artists_bp = Blueprint("artists", __name__, url_prefix="/artists")


# List all artists (Read - R in CRUD)
@artists_bp.route("/", methods=["GET"])
def index():
    artists = db.session.query(Artist).order_by(Artist.name).all()
    return render_template("artists/index.html", artists=artists)


# Show details of a specific artist (Read - R in CRUD)
@artists_bp.route("/<int:id>", methods=["GET"])
def show(id):
    artist = db.session.query(Artist).get(id)
    if artist is None:
        flash("Artist not found", "danger")
        return redirect(url_for("artists.index"))

    # Fetch the songs and albums for the artist and sort them by title
    songs = db.session.query(Song).filter_by(artist_id=id).order_by(Song.title).all()
    albums = db.session.query(Album).filter_by(artist_id=id).order_by(Album.title).all()

    return render_template(
        "artists/show.html", artist=artist, songs=songs, albums=albums
    )


# Show a form to edit an existing artist (Update - U in CRUD)
@artists_bp.route("/<int:id>/edit", methods=["GET"])
def edit(id):
    artist = Artist.query.get(id)
    if artist is None:
        flash("Artist not found", "danger")
        return redirect(url_for("artists.index"))

    return render_template("artists/edit.html", artist=artist)


# Update an existing artist (Update - U in CRUD)
@artists_bp.route("/<int:id>", methods=["POST"])
def update_artist(id):
    artist = Artist.query.get(id)
    if artist is None:
        flash("Artist not found", "danger")
        return redirect(url_for("artists.index"))

    artist.name = request.form["name"]
    artist.biography = request.form["biography"]

    db.session.commit()
    flash("Artist updated successfully!", "success")
    return redirect(url_for("artists.show", id=id))


# Delete an existing artist (Delete - D in CRUD)
@artists_bp.route("/<int:id>/delete", methods=["POST"])
def delete_artist(id):
    artist = Artist.query.get(id)
    if artist is None:
        flash("Artist not found", "danger")
        return redirect(url_for("artists.index"))

    db.session.delete(artist)
    db.session.commit()
    flash("Artist deleted successfully!", "success")
    return redirect(url_for("artists.index"))
