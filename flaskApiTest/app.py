import flask
from flask import request, jsonify
import random
import requests

app = flask.Flask(__name__)
app.config["DEBUG"] = True


apiAll = []

for i in range(1,40):
    a = {}
    trumpQuote = requests.get("https://api.whatdoestrumpthink.com/api/v1/quotes/random")
    trumpQuote = trumpQuote.json()
    trumpQuote = trumpQuote.get("message")
    a = {"id":i, "trumpQuote":trumpQuote}
    apiAll.append(a)
    
@app.route('/', methods=['GET'])
def home():
    return '''<title> Pederas </title><h1> nae nae nigga</h1>'''


@app.route('/api/all', methods=['GET'])
def api_all():
    return jsonify(apiAll)

if __name__ == "__main__":
    app.run()
