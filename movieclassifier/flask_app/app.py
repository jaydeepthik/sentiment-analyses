# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 01:16:33 2017

@author: jaydeep thik
"""

from flask import Flask, render_template
app = Flask(__name__) #ne flask instance with place to find HTML template folder

@app.route('/') #URL to trigger xecution of index function
def index():
    return render_template('first_app.html')

if __name__=="__main__":
    app.run()