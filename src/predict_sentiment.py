import pickle
import pandas as pd
from data_preprocessing import *

testTweet = pd.DataFrame([[0, 'neutral tweet']], columns=['target', 'text'])

vector_filename = 'textVetorizer.pickle'
model_filename = 'lrModel_trained.pickle'

vectorizer = pickle.load(open(vector_filename, 'rb'))
model = pickle.load(open(model_filename, 'rb'))

getCleanTweet = clean_data(testTweet)

textToPredict = getCleanTweet['text']

textToPredict_vectorized = vectorizer.transform(textToPredict)

prediction = model.predict(textToPredict_vectorized)

print(prediction)
