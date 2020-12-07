from flask import Flask

from app.routes import index


def create_app():
    """Flask application factory"""
    app = Flask(__name__)
    app.register_blueprint(index)
    return app
