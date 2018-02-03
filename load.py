# -*- coding: utf-8 -*-
# python script to load the imdb dataset into a scv file
"""
Created on Wed Sep 20 11:45:16 2017

@author: jaydeep thik
"""
import pandas as pd
import numpy as np
import os

labels = {'pos':1, 'neg':0}
df = pd.DataFrame()
for s in ('test', 'train'):
    for l in ('pos', 'neg'):
        path = 'F:/machine learning/code/sentiment analyzer/aclImdb/%s/%s' %(s, l)
        for file in os.listdir(path):
            with open(os.path.join(path, file), 'r', encoding='utf8') as infile:
                text = infile.read()
            df = df.append([[text, labels[l]]], ignore_index=True)
 
df.columns =['review', 'sentiment']

np.random.seed(0)
df = df.reindex(np.random.permutation(df.index))
df.to_csv('F:/machine learning/code/sentiment analyzer/aclImdb/movie_data.csv', index=False)           