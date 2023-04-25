from flask import render_template, flash, redirect, url_for  # render_template is a function that renders a template
from app import app  # app is an instance of the Flask class
from app.forms import LoginForm  # LoginForm is a class that represents a form


# ...

@app.route('/')  # @app.route is a decorator that tells Flask what URL should trigger the function
@app.route('/index')  # @app.route is a decorator that tells Flask what URL should trigger the function
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)