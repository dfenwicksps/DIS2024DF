import requests
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/artist_albums/<artist_id>', methods=['GET'])
def get_artist_albums(artist_id):
    api_key = '523532'
    base_url = 'https://www.theaudiodb.com/api/v1/json/{}/'.format(api_key)

    try:
        response = requests.get(base_url + 'discography.php?s=' + artist_id)
        response.raise_for_status()
        albums = response.json()['album']
        return jsonify(albums)
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=True)