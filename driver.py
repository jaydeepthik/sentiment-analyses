# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 12:24:14 2017

@author: jaydeep thik
"""

#import pandas as pd
import numpy as np
import re
#from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
#from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.linear_model import SGDClassifier 

#function to remove HTML tags, identify emoticons, remove non-words, filter stop-words
def tokenizer(text):
    text = re.sub('<[^>]*>','',text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    text = re.sub('[\W]+',' ', text.lower())+ text.join(emoticons).replace('-','')
    
    tokenized = [word for word in text.split() if word not in stop]
    
    return tokenized


  #function that reads i document at a time
def stream_docs(path):
    with open(path, 'r') as csv:
        next(csv)
        for line in csv:
            text, label = line[:-3], int(line[-2])
            yield text, label
    
#genereating mini batches of data to be fed to the SGDClassifier  
def get_minibatch(doc_stream, size):
    docs, y = [], []
    try:
        for _ in range(size):
            text, label = next(doc_stream)
            docs.append(text)
            y.append(label)
    except StopIteration:
        return None, None
    return docs, y 
    
    
stop = stopwords.words('english')

vect = HashingVectorizer(decode_error='ignore', n_features=2**21, preprocessor=None, tokenizer=tokenizer)

clf= SGDClassifier(loss='log', random_state=1 ,n_iter=1, n_jobs=-1)

doc_stream = stream_docs('F:/machine learning/code/sentiment analyzer/aclImdb/movie_data.csv') 

classes = np.array([0,1])

for _ in range(40):
    X_train, y_train = get_minibatch(doc_stream, 1000)
    X_train = vect.transform(X_train)
    clf.partial_fit(X_train, y_train, classes=classes)

X_test, y_test = get_minibatch(doc_stream, 10000)
X_test =vect.transform(X_test)
print(clf.score(X_test, y_test))
    
#df = pd.read_csv('F:/machine learning/code/sentiment analyzer/aclImdb/movie_data.csv',encoding = "ISO-8859-1")
#df['review'] = df['review'].apply(tokenizer)

print('pickeling the SGDclassifier................')
import pickle
import os

path = 'F:/machine learning/code/sentiment analyzer'
target = os.path.join(path, 'movieclassifier', 'pkl_objects')
if not os.path.exists(target):
    os.makedirs(target)

pickle.dump(stop, open(os.path.join(target, 'SGDstopwords.pkl'), 'wb'),protocol=4)
pickle.dump(clf, open(os.path.join(target, 'SGDclassifier.pkl'), 'wb'),protocol=4)

