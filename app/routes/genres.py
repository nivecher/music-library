from flask import Blueprint, render_template, flash, redirect, request, url_for
from app import db
from app.models.genre import GenreEnum

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

    return render_template("genres/show.html", genre=GenreEnum)
