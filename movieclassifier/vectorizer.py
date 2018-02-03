# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 16:03:21 2017

@author: jaydeep thik
"""

from sklearn.feature_extraction.text import HashingVectorizer
#from sklearn.feature_extraction.text import CountVectorizer
import os
import re
import pickle

cur_dir = 'F:/machine learning/code/sentiment analyzer/movieclassifier'
stop = pickle.load(open(os.path.join(cur_dir, 'pkl_objects', 'SGDstopwords.pkl'), 'rb'))

def tokenizer(text):
    text = re.sub('<[^>]*>','',text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    text = re.sub('[\W]+',' ', text.lower())+ text.join(emoticons).replace('-','')
    
    tokenized = [word for word in text.split() if word not in stop]
    
    return tokenized

h_vect = HashingVectorizer(decode_error='ignore', n_features=2**21, preprocessor=None, tokenizer=tokenizer)
#c_vect = CountVectorizer(decode_error='ignore', preprocessor=None, tokenizer=tokenizer)