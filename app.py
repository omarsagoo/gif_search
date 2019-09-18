import json
import unittest

import requests
from flask import Flask, render_template, request

import app

app = Flask(__name__)


@app.route('/')
def index():
    """Show the homepage and ask the user's name."""
    
    
    # Extract the query term from url using request.args.get()
    
    user_search = request.args.get("search")

    params = {
        "q": user_search,
        "key": "FBQJ8PNF0RXL",
        "limit": 10
    }

    # TODO: Make an API call to Tenor using the 'requests' library. For 
    # reference on how to use Tenor, see: 
    # https://tenor.com/gifapi/documentation
    response = requests.get("https://api.tenor.com/v1/search", params)

    # TODO: Use the '.json()' function to get the JSON of the returned response
    # object
    gif_json = response.json()

    # Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list
    if response.status_code == 200:
        gif_list = gif_json['results']
    else:
        gif_list = None
   
    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'
    return render_template('index.html', gifs=gif_list)


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
