# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 15:41:52 2017

@author: jaydeep thik
"""
#execute the code in console where the classifier has been trained to pickle the classifier
import pickle
import os

path = 'F:/machine learning/code/sentiment analyzer'
target = os.path.join(path, 'movieclassifier', 'pkl_objects')
if not os.path.exists(target):
    os.makedirs(target)

pickle.dump(stop, open(os.path.join(target, 'stopwords.pkl'), 'wb'),protocol=4)
pickle.dump(clf, open(os.path.join(target, 'classifier.pkl'), 'wb'),protocol=4)
    