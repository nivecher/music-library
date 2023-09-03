from app.models.genre import GenreEnum
from app import db


class Artist(db.Model):
    __tablename__ = "artists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    genre = db.Column(db.Enum(GenreEnum), nullable=True)
    country = db.Column(db.String(128), nullable=True)
    biography = db.Column(db.Text, nullable=True)
    songs = db.relationship("Song", back_populates="artist")
    albums = db.relationship("Album", back_populates="artist")

    def __init__(self, name, genre=None, country=None, biography=None):
        self.name = name
        self.genre = genre
        self.country = country
        self.biography = biography
