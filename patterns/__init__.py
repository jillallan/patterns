from config import DevConfig
from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(DevConfig)

    from .home.routes import home_bp
    from .auth.routes import auth_bp
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)

    return app
