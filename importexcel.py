# -*- coding: utf-8 -*-
"""
Created on Sun May 01 14:52:23 2016

@author: SHUBHAM
"""

import win32com.client
import scipy
import numpy as np
import matplotlib.pyplot as plt
x1 = win32com.client.gencache.EnsureDispatch("Excel.Application")
wb = x1.Workbooks('ExamProblemData.csv')
sheet = wb.Sheets('ExamProblemData')

def getdata(sheet,Range):
    data=sheet.Range(Range).Value
    data=scipy.array(data)
    data=data.reshape((1,len(data)))[0]
    return data
    
x=getdata(sheet, "D2:D11")
y=getdata(sheet, "E2:E11") 

fig=plt.figure(); ax=fig.add_subplot(111)
ax.plot(x, y, 'ro'); fig.canvas.draw()  
p=np.array(x) 
print x-y