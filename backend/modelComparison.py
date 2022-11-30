import pandas
import os

import matplotlib.pyplot as plt
from data_preprocessing import *
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import roc_curve, auc
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

#Taking the sample of the data as entire data set will hours for the model comparison
dirname = (os.path.dirname(__file__)) + "\\data\\modelComparison_sample.csv"

# we are only using a single dataset at this link so we can hardcode some stuff for training.
DATASET_COLUMNS=['target','ids','date','flag','user','text']
DATASET_ENCODING = "ISO-8859-1"
df = pd.read_csv(dirname, encoding=DATASET_ENCODING, names=DATASET_COLUMNS)

# Select required column fro mthe dataset
data = df[['text', 'target']]
data['target'] = data['target'].replace(4,1)


# Reduce dataset
data_pos = data[data['target'] == 1]
data_neg = data[data['target'] == 0]
data_pos = data_pos.iloc[:int(20000)]
data_neg = data_neg.iloc[:int(20000)]
dataset = pd.concat([data_pos, data_neg])

# The same function should be called for prediction when taking data from UI
dataset = clean_data(dataset)
# print(dataset['text'].head())

# Split dataset features and labels
X = dataset['text']
y = dataset['target']

#models
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.05, random_state =26105111)
vectorizer = TfidfVectorizer(ngram_range=(1,2), max_features=10000)

vectorizer.fit(X_train, y_train)
X_train_vectorized = vectorizer.transform(X_train)
X_test_vectorized  = vectorizer.transform(X_test)

#GaussianNB
GNB = GaussianNB()
GNB.fit(X_train_vectorized.toarray(),y_train)
y_pred1 =GNB.predict(X_test_vectorized.toarray())

# #Logistic Regression
LR = LogisticRegression()
LR.fit(X_train_vectorized.toarray(), y_train)
y_pred2 = LR.predict(X_test_vectorized.toarray())
  
# Decision Tree Classifier
DTC = DecisionTreeClassifier()
DTC.fit(X_train_vectorized.toarray(), y_train)
y_pred3 = DTC.predict(X_test_vectorized.toarray())

#Random Forest Classifier
RFC = RandomForestClassifier(random_state=42, n_jobs=-1, max_depth=5, n_estimators=100, oob_score=True)
RFC.fit(X_train_vectorized.toarray(), y_train)
y_pred4 = RFC.predict(X_test_vectorized.toarray())

#K Neighbors Ckassifier
KN = KNeighborsClassifier(n_neighbors =3)
KN.fit(X_train_vectorized.toarray(), y_train)
y_pred5 = KN.predict(X_test_vectorized)

fp1, tp1, thresholds1 = roc_curve(y_test, y_pred1)
roc_auc1= auc(fp1, tp1)
fp2, tp2, thresholds2 = roc_curve(y_test, y_pred2)
roc_auc2= auc(fp2, tp2)
fp3, tp3, thresholds3 = roc_curve(y_test, y_pred3)
roc_auc3= auc(fp3, tp3)
fp4, tp4, thresholds4 = roc_curve(y_test, y_pred4)
roc_auc4= auc(fp4, tp4)
fp5, tp5, thresholds5 = roc_curve(y_test, y_pred5)
roc_auc5= auc(fp5, tp5)

plt.figure()
plt.plot(fp1, tp1, color='darkorange', lw=1, label='ROC curve Gaussian NB (area = %0.2f)' % roc_auc1)
plt.plot(fp2, tp2, color='darkgreen', lw=1, label='ROC curve  Logistic Regression (area = %0.2f)' % roc_auc2)
plt.plot(fp3, tp3, color='purple', lw=1, label='ROC curve  Decision Tree Classifier (area = %0.2f)' % roc_auc3)
plt.plot(fp4, tp4, color='pink', lw=1, label='ROC curve  RandomForestClassifier (area = %0.2f)' % roc_auc4)
plt.plot(fp5, tp5, color='indigo', lw=1, label='ROC curve KNeighborsClassifier  (area = %0.2f)' % roc_auc5)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC CURVES ')
plt.legend(loc="lower right")
plt.show()

