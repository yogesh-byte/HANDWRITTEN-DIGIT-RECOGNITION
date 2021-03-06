# -*- coding: utf-8 -*-
"""digit_rec.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/130MBj8cqEsgzBuwgNbAb1pf94muFgkKu
"""

#import library
import pandas as pd
from sklearn import tree
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

# Read the data 
file_path = '/content/mnist_train.csv'
data = pd.read_csv(file_path)
data

data.head()

#drop the null value from the dataset
data = data.dropna()

#seprate the training dataset into inputs and target veriable
target = data["5"]

inputs = data.drop('5',axis="columns")

# split the dataset into training and testing data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(inputs,target,test_size=0.2)

#using random forest classifier(Decision tree as a base classifer)
from sklearn.ensemble import RandomForestClassifier
rf_clf = RandomForestClassifier(n_estimators=10)

rf_clf.fit(X_train,y_train)
rf_clf.score(X_test,y_test)
pred = rf_clf.predict(X_test)
pred

s = y_test.values
s

count = 0
for i in range(len(pred)):
  if pred[i] == s[i]:
    count+=1

count

len(pred)

#model accuracy
acc = count/(len(pred))
acc

#read the test dataset
file_path = '/content/test.csv'
test_data = pd.read_csv(file_path)
test_data.head()

#seprate the test dataset into target and inputs veriable 
test_inputs = test_data.drop('id',axis="columns")
test_id = test_data['id']

test_pred = rf_clf.predict(test_inputs)

sub = pd.read_csv("/content/sample_submission.csv")
sub["class"] = test_pred
sub.head()

sub.to_csv("B19EE092.csv", index=False)











