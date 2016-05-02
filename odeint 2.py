# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 23:46:58 2016

@author: SHUBHAM
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
v0=10
k1=0.5
k2=0.35
#desclare the model
def mymodel(y,t):
    dy0=v0-k1*y[0]
    dy1=k1*y[0]-k2*y[1]
    
    return [dy0,dy1]
    
time =np.linspace(0.0, 20.0, 100)
yinit=np.array([0.0,0.0])
y=odeint(mymodel,yinit,time)
plt.plot(time,y[:,0],time,y[:,1])

plt.xlabel('t')
plt.ylabel('y')
plt.show()
print y
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
a=4*10^-6
r0=0.00001;
#y0=np.array([[0.1],[0]])
#r=[0.001:0.003:0.015)
def ydot(y,t):
    y0=y[0]
    y1=y[1]
    y2=a*y0-(2/t*y1)
    
    return y1,y2
t=np.linspace(0.001,0.0015,3)
yinit=0.0,0.0
y=odeint(ydot,yinit,t)
plt.plot(t,y[:,0],t,y[:,1])

plt.xlabel('t')
plt.ylabel('y')
plt.show()
print y
"""