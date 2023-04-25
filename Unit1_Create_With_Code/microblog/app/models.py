from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary key is a unique identifier for each row in the table
    username = db.Column(db.String(64), index=True, unique=True)  # index=True creates an index for the column in the database, which improves the speed of database queries that filter on this column (e.g. SELECT * FROM users WHERE username='david') # unique=True ensures that the column will not have duplicate values (e.g. two users with the same username) # db.String(64) sets the maximum length of the string to 64 characters (the length is variable, so it can be shorter)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)
