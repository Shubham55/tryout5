# -*- coding: utf-8 -*-
"""
Created on Wed Oct 07 11:54:06 2015

@author: KAPIL
"""

import os
import pandas
import scipy
from scipy import integrate
import matplotlib.pyplot as plt


kfd=5.62E-4
kfk=5.01E-4
kfhn=3.19E-5
kfln=7.25E-5
kfg=2.45E-19
kdk=1.93E-4
kdhn=3.79E-11
kdln=6.02E-11
kdg=1.07E-11
kkhn=8.35E-4
kkln=5.31E-17
kkg=4.3E-9
khnln=5.1E-32
khng=4.39E-4
klng=8.76E-5

#nfd=0.67
#nfk=0.6
#nfhn=0.04
#nfln=0.09
#nfg=3E-16
#ndk=0.23
#ndhn=4.54E-8
#ndln=7.21E-8
#ndg=1.28E-8
#nkhn=1
#nkln=6.36E-14
#nkg=5.2E-6
#nhnln=6.11E-29
#nhng=0.5
#nlng=0.1

def deriv(c,t):
    dc0 = -(kfd+kfk+kfhn+kfln+kfg)*c[0]**2
    dc1 = kfd*c[0]**2-(kdk+kdhn+kdln+kdg)*c[1]
    dc2 = kfk*c[0]**2+kdk*c[1]-(kkhn+kkln+kkg)*c[2]
    dc3 = kfhn*c[0]**2+kdhn*c[1]+kkhn*c[2]-(khnln+khng)*c[3]
    dc4 = kfln*c[0]**2+kdln*c[1]+kkln*c[2]+khnln*c[3]-klng*c[4]
    dc5 = kfg*c[0]**2+kdg*c[1]+kkg*c[2]+khng*c[3]+klng*c[4]
    return scipy.array([dc0,dc1,dc2,dc3,dc4,dc5])
time = scipy.linspace(0,2,100)
cinit = scipy.array([912,0,0,0,0,0])
c = scipy.integrate.odeint(deriv,cinit,time)
print c[99,0]
print c[99,1]
print c[99,2]
print c[99,3]
print c[99,4]
print c[99,5]
print c[99,0]+c[99,1]+c[99,2]+c[99,3]+c[99,4]+c[99,5]

mf=c[99,0]
md=c[99,1]
mk=c[99,2]
mhn=c[99,3]
mln=c[99,4]
mg=c[99,5]
mt=c[99,0]+c[99,1]+c[99,2]+c[99,3]+c[99,4]+c[99,5]

xf=mf/mt
xd=md/mt
xk=mk/mt
xhn=mhn/mt
xln=mln/mt
xg=mg/mt
print xf*100,xd*100,xk*100,xhn*100,xln*100,xg*100






plt.plot(time,c[:,0],'r')
plt.plot(time,c[:,1],'b')
plt.plot(time,c[:,2],'g')
plt.plot(time,c[:,3],'r--')
plt.plot(time,c[:,4],'o')
plt.plot(time,c[:,5],'g^')
plt.show()






















