from flask import Flask
from flask_cors import CORS
from app.views.views_server import app_server


def create_app():
    app = Flask(__name__)
    app.register_blueprint(app_server)
    CORS(app, resource={r"/*": {"origins": "*"}})
    return app
