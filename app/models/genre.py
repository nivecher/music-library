"""_Genre classes_
"""
import sys
from app import db
from enum import Enum


class GenreEnum(Enum):
    BLUES = "Blues"
    CLASSICAL = "Classical"
    CHILDRENS = "Children's Music"
    CHRISTIAN = "Christian"
    COUNTRY = "Country"
    DANCE = "Dance"
    ELECTRONIC = "Electronic"
    FOLK = "Folk"
    HIP_HOP = "Hip Hop"
    JAZZ = "Jazz"
    LATIN = "Latin"
    POP = "Pop"
    ROCK = "Rock"
    WORLD = "Worldwide"

    def get_genre_enum(genre_string):
        try:
            genre_enum = GenreEnum(genre_string)
            return genre_enum
        except ValueError:
            print(f"Invalid Genre: {genre_string}", file=sys.stderr)
            return None


# TODO allow for extensible genres
# class Genre(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Enum(GenreEnum), nullable=False)

#     def __init__(self, name):
#         self.name = name
