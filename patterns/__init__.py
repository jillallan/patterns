from config import DevConfig
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_object=DevConfig):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config_object)

    db.init_app(app)

    with app.app_context():
        from .home.routes import home_bp
        from .auth.routes import auth_bp
        app.register_blueprint(home_bp)
        app.register_blueprint(auth_bp)

        db.create_all()

    return app
