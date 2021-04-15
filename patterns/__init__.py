from config import Config, DevConfig
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig)

    from.home import routes
    app.register_blueprint(routes.home_bp)

    return app
