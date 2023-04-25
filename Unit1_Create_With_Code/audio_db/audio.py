#!/usr/bin/env python  #step 1 import library
import json  # Step1 import libraries
import requests
from flask import Flask, render_template, request, jsonify
import urllib.request as request

# Step2 - create instance of Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'myverysectretkey'

url = "https://www.theaudiodb.com/api/v1/json/2/search.php?s=coldplay"
url = "https://www.theaudiodb.com/api/v1/json/523532/track-top10.php?s=coldplay"



@app.route('/', methods=['GET'])
def index():
    req = requests.get(url)
    source = req.text
    data = json.loads(source)
    print(type(source))
    print(source)
    print(type(data))
    print(data)
    print(data.keys())
    print(type(data['track']))
    print(data['track'])
    #print(data['track'].keys())
    mydata = data['track']

    #req.raise_for_status()
    #tracks = req.json()['track']
    #moredata = jsonify(tracks)
    #print(moredata)
    #parse_json = json.loads(data)['track']
    #key = parse_json.keys()
    #print(key)
    return render_template('index.html', data=mydata)
"""
@app.route('/', methods=['GET'])
def index():
    with request.urlopen(url) as response:
        if response.getcode() == 200:
            source = response.read()
            data = json.loads(source)
        else:
            print('An error occurred while attempting to retrieve data from the API.')
        return render_template('index.html', data=data)
"""

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8080
    app.run(debug=True)
