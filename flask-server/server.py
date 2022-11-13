from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/sentiment",  methods = ['POST'])
def sentiment():
    msg = request.json
    print("**********input msg: " + msg['inputTweet'])
    #To-do include actual model api
    return jsonify({"sentiment": "positive", "score": 9.5})

if __name__ == "__main__":
    app.run(debug=True)