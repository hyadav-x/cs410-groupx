from flask import Flask, jsonify, request
from flask_cors import CORS
from get_sentiments import *

app = Flask(__name__)
CORS(app)

@app.route("/sentiment",  methods = ['POST'])
def sentiment():
    msg = request.json
    tweet = msg['inputTweet']
    
    #Calling the model
    sentiment = get_sentiment(tweet)[0]

    print("Predicted sentiment by model:" + str(sentiment))
    if(sentiment == 1):
        return jsonify({"sentiment": "Positive"})
    else:
        return jsonify({"sentiment": "Negative"})

if __name__ == "__main__":
    app.run(debug=True)