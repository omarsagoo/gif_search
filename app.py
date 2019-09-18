import json
import unittest

import requests
from flask import Flask, render_template, request

import app

app = Flask(__name__)


@app.route('/')
def index():
    """Show the homepage and ask the user's name."""

    user_search = request.args.get("search")

    params = {
        "q": user_search,
        "key": "FBQJ8PNF0RXL",
        "limit": 10
    }

    response = requests.get("https://api.tenor.com/v1/search", params)

    gif_json = response.json()

    if response.status_code == 200:
        gif_list = gif_json['results']
    else:
        gif_list = None
    
    # if statement that checks if there is any user input, if not then it wont display any gifs. 
    # also doesnt display any gifs on startup
    if user_search == None:
        return render_template('index.html', gifs= list())
    else:
        return  render_template('index.html', gifs=gif_list)

class appTest(unittest.TestCase):

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def test_index(self):
        result = self.app.get('/')

        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()
    app.run(debug=True)
