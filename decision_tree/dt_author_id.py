#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

print(f"Number of features: {features_train.shape[1]}")

clf = DecisionTreeClassifier(min_samples_split=40)
clf.fit(features_train, labels_train)
preds = clf.predict(features_test)
print(f'Accuracy: {accuracy_score(labels_test, preds):.3f}')
