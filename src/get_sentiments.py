import pickle
import pandas as pd
from data_preprocessing import *

# Vector and model filenames
vector_filename = 'textVetorizer.pickle'
model_filename = 'lrModel_trained.pickle'

# Read the saved vecto and model files
vectorizer = pickle.load(open(vector_filename, 'rb'))
model = pickle.load(open(model_filename, 'rb'))

def get_sentiment(tweet: str):
    tweetDataset = pd.DataFrame([[0, tweet]], columns=['target', 'text'])

    tweetDataset = clean_data(tweetDataset)

    predictFor = tweetDataset['text']

    # Create vector
    predictForVectorized = vectorizer.transform(predictFor)

    prediction = model.predict(predictForVectorized)

    print("Prediction for tweet '{}': {}".format(tweet, prediction))

    return prediction