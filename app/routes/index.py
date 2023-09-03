from flask import render_template, Blueprint
from app import db
from app.models.song import Song
from app.models.artist import Artist
from app.models.album import Album
from app.models.genre import GenreEnum

index_bp = Blueprint("index", __name__)


@index_bp.route("/")
def index():
    # Count the number of records for each model
    num_songs = db.session.query(Song).count()
    num_artists = db.session.query(Artist).count()
    num_albums = db.session.query(Album).count()
    num_genres = len(GenreEnum)

    return render_template(
        "index.html",
        num_songs=num_songs,
        num_artists=num_artists,
        num_albums=num_albums,
        num_genres=num_genres,
    )
