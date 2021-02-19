from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import settings_map
from flask_session import Session

db = SQLAlchemy()


def create_app(devmode):
    app = Flask(__name__)
    setting_class = settings_map.get(devmode)
    app.config.from_object(setting_class)
    db.init_app(app)
    Session(app)
    return app
