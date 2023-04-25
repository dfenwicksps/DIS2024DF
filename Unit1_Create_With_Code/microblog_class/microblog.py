from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5001

    app.run(host, port, debug=True)