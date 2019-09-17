from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
    """Show the homepage and ask the user's name."""
    
    
    # TODO: Extract the query term from url using request.args.get()
    user_search = request.args.get("search")

    params = {
        "q": user_search,
        "key": "FBQJ8PNF0RXL",
        "limit": 10
    }

    # TODO: Make an API call to Tenor using the 'requests' library. For 
    # reference on how to use Tenor, see: 
    # https://tenor.com/gifapi/documentation
    r = requests.get("https://api.tenor.com/v1/search", params)

    # TODO: Use the '.json()' function to get the JSON of the returned response
    # object
    gif_json = r.json()

    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list
    # for i in range(len(gif_json['results'])):
    gifs = gif_json['results'] #[i]['media'][0]['gif']['url']

    return render_template('index.html', gifs=gifs)
    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'


if __name__ == '__main__':
    app.run(debug=True)

    
