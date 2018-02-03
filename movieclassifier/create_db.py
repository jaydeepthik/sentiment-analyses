# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 23:20:11 2017

@author: jaydeep thik
"""

import sqlite3

conn = sqlite3.connect('reviews.sqlite')
c=conn.cursor()
"""
c.execute('create table review_db (review text, sentiment integer, date text)')
ex1 = "this is the best movie"
c.execute("insert into review_db values(?,?,DATETIME('now'))",(ex1,1))
ex2 = "i diskike this movie"
c.execute("insert into review_db values(?,?,DATETIME('now'))",(ex2,0))"""
c.execute('select * from review_db')
data = c.fetchall()
conn.commit()
conn.close()
for i in data:
    print(i)