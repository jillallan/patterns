from os import environ, path
from dotenv import load_dotenv

base_dir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(base_dir, '.env'))


class Config:
    """Set config variables, base config"""

    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    # SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):

    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    # CSRF_ENABLED = False
