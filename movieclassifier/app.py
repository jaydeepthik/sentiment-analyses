# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 11:06:57 2017

@author: jaydeep thik
"""

from flask import render_template, Flask, request
from wtforms import TextAreaField, validators, Form
import sqlite3
import os
import numpy as np
import pickle

from vectorizer import h_vect


cur_dir = os.path.dirname(__file__)
clf = pickle.load(open(os.path.join(cur_dir, 'pkl_objects', 'SGDclassifier.pkl'), 'rb'))


db = os.path.join(cur_dir, 'reviews.sqlite')

#function to classify incoming text
def classify(text):
    label = {0:'Negative', 1:'Positive'}
    X = h_vect.transform([text])
    y = clf.predict(X)[0]
    prob = np.max(clf.predict_proba(X))
    
    if prob>0.47 and prob<0.53:
        return 'Neutral', prob
    else:
        return label[y], prob

#training for wrong classified value
def train(text, y):
    X= h_vect.transform([text])
    clf.partial_fit(X, [y])
    
#data entry into sqlite database
def sqlite_entry(path, text, y):
    conn = sqlite3.connect(path)
    
    c=conn.cursor()
    c.execute("insert into review_db values (?,?,DATETIME('now'))", (text, y))
    conn.commit()
    conn.close()
    
#initilize flask object    
app = Flask(__name__)

class ReviewForms(Form):
    moviereview = TextAreaField('',[validators.data_required(), validators.length(8)])
    
@app.route('/')
def index():
    form = ReviewForms(request.form)
    return render_template('reviewform.html', form=form)

@app.route('/results', methods=['POST'])
def results():
    form = ReviewForms(request.form)
    
    if request.method == 'POST' and form.validate():
            review = request.form['moviereview']
            y, prob = classify(review)
            
            return render_template('results.html', content=review, prediction=y, probability=round(prob*100, 2))
    return render_template('reviewform.html', form=form)

@app.route('/thanks', methods=['POST'])
def feedback():
    feedback = request.form['feedback_button']
    review = request.form['review']
    prediction = request.form['prediction']
    
    inv_label = {'Negative':0,'Positive':1}
    y=inv_label[prediction]
    
    if(feedback=='Incorrect'):
        y=int(not(y))
    train(review, y)
    sqlite_entry(db, review, y)
    return render_template('thanks.html')

if __name__=="__main__":
    app.run(debug=True)

