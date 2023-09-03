from flask import Blueprint, render_template, flash, redirect, url_for, request
from app import db
from app.models.album import Album

albums_bp = Blueprint("albums", __name__, url_prefix="/albums")


# List all albums (Read - R in CRUD)
@albums_bp.route("/", methods=["GET"])
def index():
    albums = db.session.query(Album).order_by(Album.title).all()
    return render_template("albums/index.html", albums=albums)


# Show details of a specific album (Read - R in CRUD)
@albums_bp.route("/<int:id>", methods=["GET"])
def show(id):
    album = Album.query.get(id)
    if album is None:
        flash("Album not found", "danger")
        return redirect(url_for("albums.index"))

    return render_template("albums/show.html", album=album)


# Show a form to create a new album (Create - C in CRUD)
@albums_bp.route("/create", methods=["GET"])
def create():
    return render_template("albums/new_album.html")


# Create a new album (Create - C in CRUD)
@albums_bp.route("/create", methods=["POST"])
def create_album():
    title = request.form["title"]
    release_date = request.form["release_date"]

    new_album = Album(title=title, release_date=release_date)
    db.session.add(new_album)
    db.session.commit()

    flash("Album added successfully!", "success")
    return redirect(url_for("albums.index"))


# Show a form to edit an existing album (Update - U in CRUD)
@albums_bp.route("/<int:id>/edit", methods=["GET"])
def edit(id):
    album = Album.query.get(id)
    if album is None:
        flash("Album not found", "danger")
        return redirect(url_for("albums.index"))

    return render_template("albums/edit.html", album=album)


# Update an existing album (Update - U in CRUD)
@albums_bp.route("/<int:id>", methods=["POST"])
def update_album(id):
    album = Album.query.get(id)
    if album is None:
        flash("Album not found", "danger")
        return redirect(url_for("albums.index"))

    album.title = request.form["title"]
    album.release_date = request.form["release_date"]

    db.session.commit()
    flash("Album updated successfully!", "success")
    return redirect(url_for("albums.show", album_id=id))


# Delete an existing album (Delete - D in CRUD)
@albums_bp.route("/<int:id>/delete", methods=["POST"])
def delete_album(id):
    album = Album.query.get(id)
    if album is None:
        flash("Album not found", "danger")
        return redirect(url_for("albums.index"))

    db.session.delete(album)
    db.session.commit()
    flash("Album deleted successfully!", "success")
    return redirect(url_for("albums.index"))
