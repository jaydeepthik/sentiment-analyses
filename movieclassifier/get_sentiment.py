# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 16:19:08 2017

@author: jaydeep thik
"""
from vectorizer import h_vect
import numpy as np
import os

import pickle

#cur_dir = 'F:/machine learning/code/sentiment analyzer\movieclassifier'
cur_dir = os.path.dirname(__file__)
clf = pickle.load(open(os.path.join(cur_dir, 'pkl_objects', 'SGDclassifier.pkl'), 'rb'))
lr =  pickle.load(open(os.path.join(cur_dir, 'pkl_objects', 'lr.pkl'), 'rb'))
#c_vect =pickle.load(open(os.path.join(cur_dir, 'pkl_objects' ,'c_vect.pkl'), 'rb'))
label={0:'Negative', 1:'Positive'}

example = ["one of the worst movies i have ever watched"]
example = h_vect.transform(example)
print('SGD Prediction :',label[clf.predict(example)[0]])
print('SGD Probability :',np.max(clf.predict_proba(example)))

example = ["great india's poor movie"]
example = h_vect.transform(example)

#print('\n\nLR :',label[lr.predict(example)[0]])
#print('LR :',np.max(lr.predict_proba(example)))
