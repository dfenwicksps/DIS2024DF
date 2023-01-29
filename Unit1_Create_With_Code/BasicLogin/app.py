from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # to supress warning
db = SQLAlchemy(app)

# declaring the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary key column
    title = db.Column(db.String(80), index=True, unique=True)  # book title
    author_name = db.Column(db.String(50), index=True, unique=False)  # author name
    author_surname = db.Column(db.String(80), index=True, unique=False)  # author surname
    month = db.Column(db.String(20), index=True, unique=False)  # the month of the book suggestion
    year = db.Column(db.Integer, index=True, unique=False)  # tthe year of the book suggestion

    # Get a nice printout for Book objects
    def __repr__(self):
        return "{} in: {},{}".format(self.title, self.month, self.year)


# Add your columns for the Reader model here below.
class Reader(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # insert your code here

    # get a nice printout for Reader objects
    def __repr__(self):
        return "Reader: {}".format(self.email)


# some routing for displaying the home page
@app.route('/')
@app.route('/home')
def home():
    return "Congrats! You have just made a Flask-SQLAlchemy model declaration all by yourself!"


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8080
    app.run(host, port, debug=True)