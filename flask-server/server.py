from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route("/sentiment",  methods = ['POST'])
def sentiment():
    msg = request.json
    print("**********input msg: " + msg['inputTweet'])
    #To-do include actual model api
    if(random.random() > 0.5):
        return jsonify({"sentiment": "positive", "score": 9.5})
    else:
        return jsonify({"sentiment": "negative", "score": 7.6})

if __name__ == "__main__":
    app.run(debug=True)