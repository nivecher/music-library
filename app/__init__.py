import os  # Import the os module to access environment variables
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config_by_name  # Import the configuration mapping
from app.routes.index import index_bp
from app.routes.songs import songs_bp
from app.routes.artists import artists_bp
from app.routes.albums import albums_bp
from app.routes.genres import genres_bp

# Get the environment from the FLASK_ENV environment variable
env_name = os.environ.get("FLASK_ENV", "development")

app = Flask(__name__)
app.config.from_object(config_by_name[env_name])  # Load the configuration

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Register blueprints

app.register_blueprint(index_bp)
app.register_blueprint(songs_bp)
app.register_blueprint(artists_bp)
app.register_blueprint(albums_bp)
app.register_blueprint(genres_bp)

if __name__ == "__main__":
    app.run(debug=True)
