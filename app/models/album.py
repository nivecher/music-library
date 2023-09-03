from app.models.genre import GenreEnum
from app import db


class Album(db.Model):
    __tablename__ = "albums"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    artist_id = db.Column(
        db.Integer, db.ForeignKey("artists.id", name="fk_album_artist"), nullable=True
    )
    artist = db.relationship("Artist", back_populates="albums")

    genre = db.Column(db.Enum(GenreEnum), nullable=True)

    release_date = db.Column(db.Date, nullable=True)  # Date of album release

    songs = db.relationship("Song", back_populates="album")

    def __init__(self, title, artist_id=None, genre=None, release_date=None):
        self.title = title
        self.artist_id = artist_id
        self.genre = genre
        self.release_date = release_date
