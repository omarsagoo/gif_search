import json
import unittest

import requests
from flask import Flask, render_template, request

import app

app = Flask(__name__)

def trending_gifs():
    response = requests.get("https://api.tenor.com/v1/trending?", params = {"key": "FBQJ8PNF0RXL", "limit": 9})

    gif_json = response.json()

    if response.status_code == 200:
        gif_list = gif_json['results']
    else:
        gif_list = None

    return  render_template('index.html', gifs=gif_list)

def random_gif():
    response = requests.get("https://api.tenor.com/v1/random?", params = {"key":"FBQJ8PNF0RXL", "q": "random", "limit": 9})

    gif_json = response.json()

    if response.status_code == 200:
        gif_list = gif_json['results']
    else:
        gif_list = None

    return  render_template('index.html', gifs=gif_list)

def search_gif(user_search):
    params = {
    "q": user_search,
    "key": "FBQJ8PNF0RXL",
    "limit": 9
    }

    response = requests.get("https://api.tenor.com/v1/search", params)
    gif_json = response.json()

    if response.status_code == 200:
        gif_list = gif_json['results']
    else:
        gif_list = None
    
    return  render_template('index.html', gifs=gif_list)

@app.route('/')
def index():
    """Show the homepage and ask the user's name."""
    # accepts user input from the html and passes it in to the query param
    user_search = request.args.get("search")

    # stores params in a dict variable for the api respponse

    if request.args.get("trending") == "trending":
        return trending_gifs()
    elif request.args.get("random") == "random":
        return random_gif()
    elif request.args.get("search") != None: 
        return search_gif(user_search)
    else:
        return  render_template('index.html', gifs=list())

    #retrieves the API response 


    # stores the api response in json in a dict variable

    # Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list
    
    
    # if statement that checks if there is any user input, if not then it wont display any gifs. 
    # also doesnt display any gifs on startup
    

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
