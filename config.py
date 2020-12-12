import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config():

    # General config
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_APP = 'wsgi.py'
    FLASK_ENV = 'development'

    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Static assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
