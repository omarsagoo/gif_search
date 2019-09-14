from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

def input_handler(prompt):
    user_input = input(prompt)

    return user_input

@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract the query term from url using request.args.get()

    params = {
        "key": "FBQJ8PNF0RXL",
        "q": input_handler("what kind of gif? "),
        "limit": 10
    }

    # TODO: Make an API call to Tenor using the 'requests' library. For 
    # reference on how to use Tenor, see: 
    # https://tenor.com/gifapi/documentation
    response = requests.get("https://api.tenor.com/v1/search", params)

    # TODO: Use the '.json()' function to get the JSON of the returned response
    # object
    gif_json = response.json()

    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list
    for i in range(len(gif_json['results'])):
        gif_list = gif_json['results'] #[i]['media'][0]['gif']['url']
        print(gif_list)

    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'

    return render_template("index.html", gif_list = gif_list)

if __name__ == '__main__':
    app.run(debug=True)

    
