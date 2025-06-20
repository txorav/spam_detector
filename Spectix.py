# import polars as pandas fast alternative due to usage of Rust
import polars as pl

# import numpy to convert vectors to arrays
import numpy as np

# import linear_model where we find logistic regression
from sklearn import linear_model

# import linear_model where we find naive bayes
from sklearn.naive_bayes import MultinomialNB

# import decision tree classifier
from sklearn.tree import DecisionTreeClassifier

# import k-nearest value
from sklearn.neighbors import KNeighborsClassifier

# import support vector machine
from sklearn.svm import SVC

# import random forest classifier
from sklearn.ensemble import RandomForestClassifier

# import gradient boosting
from sklearn.ensemble import GradientBoostingClassifier

# import neural network
from sklearn.neural_network import MLPClassifier

# import pipeline to use ML algorithm while vectorizing text
from sklearn.pipeline import make_pipeline

# import vectorizer that will convert text into vectors
from sklearn.feature_extraction.text import TfidfVectorizer

# import joblib that is used to dump the model
import joblib

# import numpy to convert matrix to vectors
import numpy as np

# import matplotlib to show the plot of x and y
import matplotlib.pyplot as plt

# first read the csv using polars
df = pl.read_csv('/content/drive/MyDrive/email_spam_detection_final.csv')

# import csv to remove the csv limit
import csv

# randomize the dataset
# df = df.sample(fraction=1.0,with_replacement=False,seed=123)

# remove the csv limit
csv.field_size_limit(100000000)


# print the df to check
print(df)

# separate the training data and desired data
x = df["body"][10000:].fill_null(' ')
y = df['label'][10000:]

# make test data
tst_x = df["body"][0:10000].fill_null(' ')
tst_y = df["label"][0:10000]

# make pipeline logistic regression
model_lr = make_pipeline(TfidfVectorizer(),linear_model.LogisticRegression())

# make pipeline naive bayes
model_nb = make_pipeline(TfidfVectorizer(),MultinomialNB())

# make pipeline decision tree classifier
model_dt = make_pipeline(TfidfVectorizer(),DecisionTreeClassifier())

# make pipline k-nearest value
model_knn = make_pipeline(TfidfVectorizer(),KNeighborsClassifier())

# make pipeline support vector machine
model_svm = make_pipeline(TfidfVectorizer(),SVC())

# make pipeline for random forest classifier
model_rf = make_pipeline(TfidfVectorizer(),RandomForestClassifier())

# make pipeline for gradient boosting classifier
model_gb = make_pipeline(TfidfVectorizer(),GradientBoostingClassifier())

# make pipeline for neural network
model_nn = make_pipeline(TfidfVectorizer(),MLPClassifier())

#train the model
#logistic regression
print("training model 1 ( logistic regression ).....")
model_lr.fit(x,y)
print("training model 1 ( logistic regression ) done")
# naive bayes
print("training model 2 ( naive bayes ).....")
model_nb.fit(x,y)
print("training model 2 ( naive bayes ) done")
#decision tree classifier
print("training model 3 ( decision tree classifier ).....")
model_dt.fit(x,y)
print("training model 3 ( decision tree classifier ) done")
# k-nearest value
print("training model 4 ( k-nearest value ).....")
model_knn.fit(x,y)
print("training model 4 ( k-nearest value ) done")
# support vector machine
print("training model 5 ( support vector machine ).....")
model_svm.fit(x,y)
print("training model 5 ( support vector machine ) done")
# random forest classifier
print("training model 6 ( random forest classifier ).....")
model_rf.fit(x,y)
print("training model 6 ( random forest classifier ) done")
# gradient boosting classifier
print("training model 7 ( gradient boosting classifier ).....")
model_gb.fit(x,y)
print("training model 7 ( gradient boosting classifier ) done")
# neural network
print("training model 8 ( neural network ).....")
model_nn.fit(x,y)
print("training model 8 ( neural network ) done")

#dump the model
joblib.dump(model_lr,'spamdet_lr.pk1')
joblib.dump(model_nb,'spamdet_nb.pk1')

model_lr = joblib.load('spamdet_lr.pk1')
model_nb = joblib.load('spamdet_nb.pk1')
joblib.dump(model_dt,'spamdet_dt.pk1')
joblib.dump(model_knn,'spamdet_knn.pk1')
joblib.dump(model_svm,'spamdet_svm.pk1')
joblib.dump(model_rf,'spamdet_rf.pk1')
joblib.dump(model_gb,'spamdet_gb.pk1')
joblib.dump(model_nn,'spamdet_nn.pk1')

# function to find accuracy
def verify_accuracy (tstx,tsty,model):
  res = 0
  for i in range(0,10000):
    resu = int(model.predict([tstx[i]])[0]) == tsty[i]
    if resu == True :
      res = res + 1
    else :
      continue
  result = res/10000
  print(result)

model_dt = joblib.load('spamdet_dt.pk1')
model_knn = joblib.load('spamdet_knn.pk1')

model_svm = joblib.load('spamdet_svm.pk1')
model_rf = joblib.load('spamdet_rf.pk1')

#verify model accuracy
verify_accuracy(tst_x,tst_y,model_lr)
verify_accuracy(tst_x,tst_y,model_nb)
verify_accuracy(tst_x,tst_y,model_dt)
verify_accuracy(tst_x,tst_y,model_knn)
verify_accuracy(tst_x,tst_y,model_svm)
verify_accuracy(tst_x,tst_y,model_rf)
verify_accuracy(tst_x,tst_y,model_gb)
verify_accuracy(tst_x,tst_y,model_nn)