# utilities
import re
import numpy as np
import pandas as pd
import string

# nltk
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

STOPWORDS = set(stopwords.words('english'))
st = nltk.PorterStemmer()
lm = nltk.WordNetLemmatizer()

# Remove URLs
def cleaning_URLs(data):
    return re.sub('((www.[^s]+)|(https?://[^s]+))',' ',data)

# Remove punctuation
# english_punctuations = string.punctuation
# punctuations_list = english_punctuations

def cleaning_punctuations(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

# Remove repeating characters
def cleaning_repeating_char(text):
    return re.sub(r'(.)1+', r'1', text)

# Remove stop words
def cleaning_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])

# Remove numbers
def cleaning_numbers(data):
    return re.sub('[0-9]+', '', data)

# Stemming
def stemming_on_text(data):
    text = [st.stem(word) for word in data]
    return data

# Lemmatize
def lemmatizer_on_text(data):
    text = [lm.lemmatize(word) for word in data]
    return data

def clean_data(dataset):

    # The function cleans the datasent send as dataframe and returns a dataframe
    # for the machine learning pipeline
    
    # Remove URLs
    dataset['text'] = dataset['text'].apply(lambda x: cleaning_URLs(x))

    # Remove punctuations
    dataset['text']= dataset['text'].apply(lambda x: cleaning_punctuations(x))

    # Remove repeating characters
    dataset['text'] = dataset['text'].apply(lambda x: cleaning_repeating_char(x))

    # Convert to lower
    dataset['text'] = dataset['text'].str.lower()

    # Remove stop words
    dataset['text'] = dataset['text'].apply(lambda text: cleaning_stopwords(text))

    # Remove numbers
    dataset['text'] = dataset['text'].apply(lambda x: cleaning_numbers(x))

    # Tokenize
    tokenizer = RegexpTokenizer("[\w']+")
    dataset['text'] = dataset['text'].apply(tokenizer.tokenize)

    # Perform stemming
    dataset['text']= dataset['text'].apply(lambda x: stemming_on_text(x))

    # Lemantize
    dataset['text'] = dataset['text'].apply(lambda x: lemmatizer_on_text(x))

    # Convert text to string
    # This is done for vectorizer
    dataset['text'] = [' '.join(map(str, l)) for l in dataset['text']]  

    return dataset