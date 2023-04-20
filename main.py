from flask import Flask, render_template, request, jsonify
import os
import requests

app = Flask(__name__)
MAL_CLIENT_ID = os.getenv("MAL_CLIENT_ID")
MAL_SECRET = os.getenv("MAL_SECRET")
AUTH_HEADER = {
        'X-MAL-CLIENT-ID': MAL_CLIENT_ID
    }

@app.route('/')
def index():
    return render_template('index.html')
    # return "<h1> hello world </h1>"

@app.route('/anime-list', methods=['GET'])
def get_anime_list():
    username = request.args.get('username')
    print(username)

    anime_list = []
    response = requests.get("https://api.myanimelist.net/v2/users/{}/animelist?fields=list_status&limit=1000&sort=list_score&status=completed".format(username), headers=AUTH_HEADER)
    if response.status_code == 200:
        anime_list = response.json()['data']

    print(response.headers)
    print()
    print()
    print(anime_list)

    return jsonify(anime_list)