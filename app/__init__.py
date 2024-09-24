from flask import Flask
from .db import init_db
from .routes import api_bp


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@192.168.6.100/wl_test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    init_db(app)
    app.register_blueprint(api_bp)

    return app
