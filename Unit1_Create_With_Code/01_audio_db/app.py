from flask import Flask, render_template, request
import requests
import sqlite3

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        artist_name = request.form['artist']
        albums = search_albums(artist_name)
        save_albums_to_db(artist_name, albums)
        return render_template('results.html', artist=artist_name, albums=albums)
    return render_template('index.html')


def search_albums(artist_name):
    API_KEY = 'my_api_key'
    URL = f'https://theaudiodb.com/api/v1/json/{API_KEY}/searchalbum.php?s={artist_name}'
    response = requests.get(URL)
    data = response.json()
    albums = data['album']
    return albums


def save_albums_to_db(artist_name, albums):
    conn = sqlite3.connect('albums.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS albums
                 (artist TEXT, album TEXT, year INTEGER)''')

    for album in albums:
        c.execute("INSERT INTO albums VALUES (?,?,?)", (artist_name, album['strAlbum'], album['intYearReleased']))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    app.run(debug=True)
