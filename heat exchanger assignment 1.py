# -*- coding: utf-8 -*-
"""
Created on Sun Jan 03 22:17:36 2016

@author: Shubham Deshmane
"""

import scipy 
import matplotlib.pyplot as plt
import scipy.optimize as opti

mh=1 #(kg/s)
mc=1 #(kg/s)
Thin=400 #all temp in K
Tcin=300 
U=100 #W/m2K
L=10 #m2
n=10
Thguess=n*[Thin] 
Tcguess=n*[Tcin] 
Tguess=scipy.array(Thguess+Tcguess) 
def CpH(T):
    CpH=4.184+(10**-9)*T**3+(10**-6)*T**2+(10**-4)*T
    return CpH

def CpC(T):
    CpC=4.184+(10**-9)*T**3+(10**-6)*T**2+(10**-4)*T
    return CpC
def residuals(T,U,L,Thin,Tcin,mh,mc):
    n=len(T)
    Th=T[:n/2] 
    Tc=T[n/2:]
    dA=L/((n-1) 
    errHLs=(U*(Thin-Tc[0])/(mh*CpH(Thin)))+((Th[1]-Thin)/dA)
    errCLs=(U*(Thin-Tc[0])/(mc*CpC(Tc[0])))+((Tc[1]-Tc[0])/dA)
    errHRs=(U*(Th[-1]-Tcin)/(mh*CpH(Th[-1])))+((Th[-1]-Th[-2])/dA)
    errCRs=(U*(Th[-1]-Tcin)/(mc*CpC(Tcin)))+((Tcin-Tc[-2])/dA)
    errH=scipy.zeros(n/2)
    errC=scipy.zeros(n/2)
    errH[0]=errHLs; errH[-1]=errHRs
    errC[0]=errCLs;errC[-1]=errCRs
    errH[1:-1]=(U*(Th[1:-1]-Tc[1:-1])/(mh*CpH(Th[1:-1])))+((Th[2:])-Th[1:-1])/dA
    errC[1:-1]=(U*(Th[1:-1]-Tc[1:-1])/(mc*CpC(Tc[1:-1])))+((Tc[2:])-Tc[1:-1])/dA
    return scipy.concatenate((errH,errC))
    
n=len(Tguess)   
soln=opti.leastsq(residuals,Tguess,args=(U,A,Thin,Tcin,mh,mc))
print (soln)
Tsoln=soln[0]
Thsoln=Tsoln[:n/2]
Thsoln[0]=Thin
Tcsoln=Tsoln[n/2:]
Tcsoln[-1]=Tcin
print (Thsoln)
print (Tcsoln)
b=scipy.linspace(0, 100,10)
#plt.plot(b, Thsoln,'r')
#plt.show()
plt.plot(b,Tcsoln,'b')
plt.show()
    