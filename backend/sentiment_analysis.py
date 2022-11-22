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

# sklearn
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix, classification_report

# Pickle
import pickle

DATASET_COLUMNS=['target','ids','date','flag','user','text']
DATASET_ENCODING = "ISO-8859-1"
df = pd.read_csv('data/training.1600000.processed.noemoticon.csv', encoding=DATASET_ENCODING, names=DATASET_COLUMNS)

# Select required column fro mthe dataset
data = df[['text', 'target']]
data['target'] = data['target'].replace(4,1)


# Reduce dataset
data_pos = data[data['target'] == 1]
data_neg = data[data['target'] == 0]
data_pos = data_pos.iloc[:int(20000)]
data_neg = data_neg.iloc[:int(20000)]

dataset = pd.concat([data_pos, data_neg])
dataset = pd.concat([data_pos, data_neg])

#print(dataset['text'].head())

# Remove URLs
def cleaning_URLs(data):
    return re.sub('((www.[^s]+)|(https?://[^s]+))',' ',data)
dataset['text'] = dataset['text'].apply(lambda x: cleaning_URLs(x))

# Remove punctuation
english_punctuations = string.punctuation
punctuations_list = english_punctuations

def cleaning_punctuations(text):
    translator = str.maketrans('', '', punctuations_list)
    return text.translate(translator)
dataset['text']= dataset['text'].apply(lambda x: cleaning_punctuations(x))

# Remove repeating characters
def cleaning_repeating_char(text):
    return re.sub(r'(.)1+', r'1', text)
dataset['text'] = dataset['text'].apply(lambda x: cleaning_repeating_char(x))

# convert to lower
dataset['text'] = dataset['text'].str.lower()

# Remove stop words
STOPWORDS = set(stopwords.words('english'))
def cleaning_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])
dataset['text'] = dataset['text'].apply(lambda text: cleaning_stopwords(text))

# Remove numbers
def cleaning_numbers(data):
    return re.sub('[0-9]+', '', data)
dataset['text'] = dataset['text'].apply(lambda x: cleaning_numbers(x))


# Tokenize
tokenizer = RegexpTokenizer("[\w']+")
dataset['text'] = dataset['text'].apply(tokenizer.tokenize)

# Stemming
st = nltk.PorterStemmer()
def stemming_on_text(data):
    text = [st.stem(word) for word in data]
    return data
dataset['text']= dataset['text'].apply(lambda x: stemming_on_text(x))


# Lemmatize
lm = nltk.WordNetLemmatizer()
def lemmatizer_on_text(data):
    text = [lm.lemmatize(word) for word in data]
    return data
dataset['text'] = dataset['text'].apply(lambda x: lemmatizer_on_text(x))

print(dataset['text'].head())

# Convert text to string
dataset['text'] = [' '.join(map(str, l)) for l in dataset['text']]

print(dataset['text'].head())

X = dataset['text']
y = dataset['target']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.05, random_state =26105111)

vectorizer = TfidfVectorizer(ngram_range=(1,2), max_features=500000)

vectorizer.fit(X_train, y_train)
X_train_vectorized = vectorizer.transform(X_train)
X_test_vectorized  = vectorizer.transform(X_test)


def model_Evaluate(model):
# Predict values for Test dataset
    y_pred = model.predict(X_test_vectorized)
    # Print the evaluation metrics for the dataset.
    print(classification_report(y_test, y_pred))

# bnbmodel = BernoulliNB()
# bnbmodel.fit(X_train_vectorized, y_train)
# model_Evaluate(bnbmodel)
# y_pred1 = bnbmodel.predict(X_test_vectorized)

lrModel = LogisticRegression(C = 2, max_iter = 1000, n_jobs=-1)
lrModel.fit(X_train_vectorized, y_train)

model_filename = 'lrModel_trained.sav'
pickle.dump(lrModel, open(model_filename, 'wb'))

sampleTweet = ["I like machine learning."]
inputData = pd.DataFrame(sampleTweet, columns=['text'])