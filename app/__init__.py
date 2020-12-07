from dotenv import load_dotenv
from flask import Flask
from os import environ
from flask_migrate import Migrate

from app.routes import index
from app.models import bcrypt, db

load_dotenv(verbose=True)


def create_app():
    """Flask application factory"""
    app = Flask(__name__)
    app.config.from_mapping(
        BCRYPT_LOG_ROUNDS=10,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_DATABASE_URI=environ["ELIT_LINKER_DATABASE_URI"]
    )
    bcrypt.init_app(app)
    db.init_app(app)
    Migrate(app, db)
    app.register_blueprint(index)
    return app
