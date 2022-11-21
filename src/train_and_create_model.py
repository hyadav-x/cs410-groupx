# import data cleaning
from data_preprocessing import *

# sklearn
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix, classification_report

# pickel
import pickle

# we are only using a single dataset at this link so we can hardcode some stuff for training.
DATASET_COLUMNS=['target','ids','date','flag','user','text']
DATASET_ENCODING = "ISO-8859-1"
df = pd.read_csv('data/training.1600000.processed.noemoticon.csv', encoding=DATASET_ENCODING, names=DATASET_COLUMNS)

# Select required column fro mthe dataset
data = df[['text', 'target']]
data['target'] = data['target'].replace(4,1)


# Reduce dataset
# remove this later
data_pos = data[data['target'] == 1]
data_neg = data[data['target'] == 0]
data_pos = data_pos.iloc[:int(20000)]
data_neg = data_neg.iloc[:int(20000)]

dataset = pd.concat([data_pos, data_neg])

# The same function should be called for prediction when taking data from UI
dataset = clean_data(dataset)

print(dataset['text'].head())

# Split dataset features and labels
X = dataset['text']
y = dataset['target']


# This is to check the model
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.05, random_state =26105111)

vectorizer = TfidfVectorizer(ngram_range=(1,2), max_features=500000)

vectorizer.fit(X_train, y_train)
X_train_vectorized = vectorizer.transform(X_train)
X_test_vectorized  = vectorizer.transform(X_test)

lrModel = LogisticRegression(C = 2, max_iter = 1000, n_jobs=-1)
lrModel.fit(X_train_vectorized, y_train)

vector_filename = 'textVetorizer.pickle'
model_filename = 'lrModel_trained.pickle'

pickle.dump(vectorizer, open(vector_filename, 'wb'))
pickle.dump(lrModel, open(model_filename, 'wb'))
