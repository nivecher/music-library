# models/song.py

from app import db
from app.models.genre import GenreEnum


class Song(db.Model):
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id"), nullable=True)
    album_id = db.Column(db.Integer, db.ForeignKey("albums.id"), nullable=True)
    genre = db.Column(db.Enum(GenreEnum), nullable=True)
    duration = db.Column(db.String(8), nullable=True)  # Format: "hh:mm:ss"

    artist = db.relationship("Artist", back_populates="songs")
    album = db.relationship("Album", back_populates="songs")

    def __init__(
        self,
        title,
        artist_id,
        album_id=None,
        genre=None,
        duration=None,
    ):
        self.title = title
        self.artist_id = artist_id
        self.album_id = album_id
        self.genre = genre
        self.duration = duration
