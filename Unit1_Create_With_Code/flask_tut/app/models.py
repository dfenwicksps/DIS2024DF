from datetime import datetime  # datetime is a class that represents a date and time, from the datetime module
from app import db  # db is an instance of SQLAlchemy class, which represents the database, from app/__init__.py
from werkzeug.security import generate_password_hash  #
class User(db.Model):  # User is a class that represents a user, db.Model is a base class for all models from Flask-SQLAlchemy, it contains common methods for classes that represent database tables
    id = db.Column(db.Integer, primary_key=True)  # id is a column in the users table that stores the user's id, db.Column is a class that represents a column in a database table, db.Integer is a type for integer values, primary_key=True means that this column is the primary key
    username = db.Column(db.String(64), index=True, unique=True)  # username is a column in the users table that stores the user's username, db.String is a type for string values, 64 is the maximum length of the string, index=True means that this column will be indexed, unique=True means that the value in this column must be unique
    email = db.Column(db.String(120), index=True, unique=True)  # email is a column in the users table that stores the user's email, db.String is a type for string values, 120 is the maximum length of the string, index=True means that this column will be indexed, unique=True means that the value in this column must be unique
    password_hash = db.Column(db.String(128))  # password_hash is a column in the users table that stores the user's password hash, db.String is a type for string values, 128 is the maximum length of the string
    posts = db.relationship('Post', backref='author', lazy='dynamic')  # posts is a column in the users table that stores the user's posts, db.relationship is a class that represents a one-to-many relationship, 'Post' is the name of the class that represents the other side of the relationship, backref is a field that will be added to the objects of the "many" class that points back at the "one" object, lazy defines when SQLAlchemy will load the data from the database, dynamic means that the loading will be performed in a separate query

    def __repr__(self):  # __repr__ is a special method that is used to compute the "official" string representation of an object, it is used for debugging and logging
        return '<User {}>'.format(self.username)  # return a string that represents the user, it is used for debugging and logging, it is called by print() and str()

class Post(db.Model):  # Post is a class that represents a post, db.Model is a base class for all models from Flask-SQLAlchemy, it contains common methods for classes that represent database tables
    id = db.Column(db.Integer, primary_key=True)  # id is a column in the posts table that stores the post's id, db.Column is a class that represents a column in a database table, db.Integer is a type for integer values, primary_key=True means that this column is the primary key
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
