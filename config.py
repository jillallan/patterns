from os import path
from dotenv import load_dotenv

base_dir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(base_dir, '.env'))


class Config:
    """Set config variables, base config"""

    FLASK_APP = 'patterns'


class DevConfig(Config):

    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
