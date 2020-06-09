import datetime

from flask import Flask
from flask_cors import CORS

from .config.default import DefaultConfig
from .views import register_blueprints
from .cache import cache
from .models import db


__version__ = '1.0'
__status__ = 'dev'
__description__ = 'Your project description'
__github__ = 'Your Git address'
__license__ = "MIT License"


def create_app():
    app = Flask(__name__)
    # 数据库配置
    app.config['SQLALCHEMY_DATABASE_URI'] = DefaultConfig.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_BINDS'] = DefaultConfig.SQLALCHEMY_BINDS
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = DefaultConfig.SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['SECRET_KEY'] = DefaultConfig.SECRET_KEY
    app.permanent_session_lifetime = datetime.timedelta(seconds=DefaultConfig.SESSION_TIME)
    register_blueprint(app)
    register_database(app)
    cache.init_app(app, config=DefaultConfig.FILESYSTEM)
    CORS(app, supports_credentials=True)
    return app


def register_database(app):
    db.init_app(app)
    db.app = app


def register_blueprint(app):
    register_blueprints(app)
