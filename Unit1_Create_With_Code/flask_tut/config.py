import os  # os module provides functions for interacting with the operating system

basedir = os.path.abspath(os.path.dirname(__file__))  # path to the directory where the config.py file is located

class Config(object):  # Config is a class that stores configuration variables, it is a base class for all configuration classes
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'  # SECRET_KEY is a configuration variable that is used by Flask and extensions to keep data safe, it is set to a random value
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')  # SQLALCHEMY_DATABASE_URI is a configuration variable that is the database connection URI, it is set to a SQLite database file in the app directory
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # SQLALCHEMY_TRACK_MODIFICATIONS is a configuration variable that is set to False to disable a feature that I don't need
