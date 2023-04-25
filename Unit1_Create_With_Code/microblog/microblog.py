from app import app


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5001
    app.run(host, port, debug=True)