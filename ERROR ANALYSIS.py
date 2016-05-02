# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 19:12:14 2016

@author: Shubham Deshmane
"""
import win32com.client
import scipy,scipy.optimize
import matplotlib.pyplot as plt
#import numpy as np
#from scipy import array
#x=array([1164.42,1663.97,1950.45,3526.04,4319.63])
#y=array([.03188,.03122,.025,.0125,.01158])
#print y
"""following is the syntax fr data import frm excel
using win32.com""" 
x1=win32com.client.gencache.EnsureDispatch("Excel.Application")
wb=x1.Workbooks('data.xlsx')
sheet=wb.Sheets('data')
"""defined function get data for sheet""" 
def getdata(sheet,Range):
    data=sheet.Range(Range).Value
    data=scipy.array(data)
    data=data.reshape((1,len(data)))[0]
    return data
    
x=getdata(sheet,"D5:D10")
y=getdata(sheet,"E5:E10")
""" curve function for y=c1*x**c2"""
def curve(x,p):
    [c1,c2]=p
    y=c1*x**c2
    return y
def residual(p,x,y):
    e=y-curve(x,p)
    return e
    """to find error"""
def get_r2(x,y,ycalc):
    ymean=scipy.average(y)
    dymean2=(y-ymean)**2
    dycalc2=(y-ycalc)**2
    RSQUARE=1-sum(dycalc2)/sum(dymean2)
    return RSQUARE
pguess=[16,-1]
plsq=scipy.optimize.leastsq(residual,pguess,args=(x,y))
p=plsq[0]
ycalc=curve(x,p)
RSQUARE=get_r2(x,y,ycalc)
print p
""" syntax for graph"""
fig=plt.figure();
ax=fig.add_subplot(111)
ax.plot(x,y,'+')
ax.plot(x,ycalc,'g')    
ax.title.set_text('rsquare=%f'%(RSQUARE))
fig.canvas.draw()
plt.show()

#import win32com.client
#import scipy
#import matplotlib.pyplot as plt

"""x1=win32com.client.gencache.EnsureDispatch("Excel.Application")
wb=x1.Workbooks('data.xlsx')
sheet=wb.Sheets('data')
 
def getdata(sheet,Range):
    data=sheet.Range(Range).Value
    data=scipy.array(data)
    data=data.reshape((1,len(data)))[0]
    return data
    
x=getdata(sheet,"D5:D10")
y=getdata(sheet,"E5:E10")
"""
