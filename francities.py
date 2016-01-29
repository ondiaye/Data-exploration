# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 14:33:02 2016

@author: OumouKalsoum
"""

import os
import sqlite3
from win32com.client import Dispatch

#----------------------------------------
# get data from excel file
#----------------------------------------
XLS_FILE = os.getcwd() + "\\TCRD_043.xls"
ROW_SPAN = (14, 21)
COL_SPAN = (2, 7)
app = Dispatch("Excel.Application")
app.Visible = True
ws = app.Workbooks.Open(XLS_FILE).Sheets(1)
exceldata = [[ws.Cells(row, col).Value 
              for col in xrange(COL_SPAN[0], COL_SPAN[1])] 
             for row in xrange(ROW_SPAN[0], ROW_SPAN[1])]

#----------------------------------------
# create SQL table and fill it with data
#----------------------------------------
conn = sqlite3.connect('france.db')
c = conn.cursor()
c.execute('''CREATE TABLE if not exists francedata (
   id INTEGER,
   name TEXT,
   densite  INTEGER,
   superficie INTEGER,
   nbrecom INTEGER
)''')
for row in exceldata:
    c.execute('INSERT INTO francedata VALUES (?,?,?,?,?)', row)
conn.commit()

#----------------------------------------
# display SQL data
#----------------------------------------
c.execute('SELECT * FROM francedata')
for row in c:
    print row

conn.close    