import os

basedir = os.path.abspath(os.path.dirname(__file__))  # sets the base directory for the application to the directory of the config.py file (the root directory)

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY' or 'a-string-you-will-never-guess')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')  # sets the type and location of the database file
    SQLALCHEMY_TRACK_MODIFICATIONS = False
