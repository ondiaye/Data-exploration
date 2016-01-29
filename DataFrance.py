# -*- coding: utf-8 -*-
"""
Created on Thu Dec 03 00:00:41 2015

@author: OumouKalsoum
"""
import sqlite3
import csv

conn = sqlite3.connect('‪france.db')
conn.text_factory = str 
cur = conn.cursor()
data = cur.execute("select id, name,densite from francedata")

with open('Datafran.csv', 'wb') as f:
    writer = csv.writer(f, delimiter = ';')
    writer.writerow(['id','name','densite'])
    writer.writerows(data)

conn.close

