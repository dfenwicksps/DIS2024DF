from flask import Flask  # Flask is a class that represents the web application
from Unit1_Create_With_Code.flask_tut.config import Config  # Config is a class that stores configuration variables
from flask_sqlalchemy import SQLAlchemy  # handles db operations
from flask_migrate import Migrate  # handles db migrations

app = Flask(__name__)  # app is an instance of Flask class
app.config.from_object(Config)  # app.config is a dictionary that stores configuration variables

db = SQLAlchemy(app)  # db is an instance of SQLAlchemy class, which represents the database
migrate = Migrate(app, db)  # migrate is an instance of Migrate class, which handles db migrations

from app import routes, models, forms  # routes and models are modules that contain code for the application