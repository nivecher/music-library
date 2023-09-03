from flask import Blueprint

# Import routes from individual modules
from app.routes.index import *
from app.routes.songs import *
from app.routes.artists import *
from app.routes.albums import *
from app.routes.genres import *

# Define blueprints for different sections of your music library app
index_bp = Blueprint("index", __name__)
songs_bp = Blueprint("songs", __name__)
artists_bp = Blueprint("artists", __name__)
albums_bp = Blueprint("albums", __name__)
genres_bp = Blueprint("genres", __name__)
