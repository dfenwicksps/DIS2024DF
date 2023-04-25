import os
from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or \
    'e5ac358c-f0bf-11e5-9e39-d3b532c10a28'

@app.route('/')
#def hello_world():
#    return "<p>Hello, World!</p>"
def index():
    data = "hello everyone"
    #return redirect(url_for('index')
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.debug = True
    app.run()