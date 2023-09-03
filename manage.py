from mimetypes import init
from flask.cli import FlaskGroup
from app import create_app, db

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command("init-db")
def init_db():
    """Initialize the database."""
    print("Dropping database...")
    db.drop_all()
    print("Creating database...")
    db.create_all()
    print("Database initialized.")


if __name__ == "__main__":
    cli()
