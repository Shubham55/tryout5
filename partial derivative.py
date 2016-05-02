# -*- coding: utf-8 -*-
"""
Created on Sun Feb 07 11:29:06 2016

@author: Shubham Deshmane
"""
import scipy
import numpy as np
Dhg=1437
Dw=1000
u=0.001
D=0.0209
#i=0
Q=[27.6*10**-6,34*10**-6,35.6*10**-6,40.4*10**-6]
#reynolds number calc
#1)
Rei_list=[]
for i in range(len(Q)):
    Rei=4*Q[i]*Dw/(3.14*D*u)
    Rei_list.append(Rei)#Rei=4*i*Dw/(3.14*D*u)
Rei_list=np.array(Rei_list)
print Rei_list  
delRe_D_list=[]  
#2) 
for i in range(len(Q)):
    delRe_D=((-4*Q[i]*Dw)/(3.14*u*D**2))  
    delRe_D_list.append(delRe_D)
delRe_D_list=np.array(delRe_D_list)
print delRe_D_list
delRe_Q_list=[] 
#3)
for i in range(len(Q)):
    delRe_Q=((4*Dw)/(3.14*u*D))
    delRe_Q_list.append(delRe_Q)    
delRe_Q_list=np.array(delRe_Q_list)
print delRe_Q_list

delRe_i_list=[]
for i in range(len(delRe_Q_list)) and range(len(delRe_D_list)):
    delRe_i=((delRe_Q_list)**2+(delRe_D_list)**2)**0.5
    delRe_i_list.append(delRe_i)
delRe_i_list=np.array(delRe_i_list)
print delRe_i_list

"""i=0;
for delRei in delRe_Q and delRe_D:
    delRei[i]=((delRe_Q[i])**2+(delRe_D[i])**2)**0.5
    i=i+1
    print delRei
"""
#friction factor calc
delta_h=[0.002,0.003,0.005,0.008]
L=2.52;i=0 

f_i_list=[]
for i in range(len(Q)) and range(len(delta_h)):
    f_i=(delta_h[i]*(Dhg-Dw)*9.8*D**5*3.14**2)/(32*Dw*Q[i]**2*L)    
    f_i_list.append(f_i)
f_i_list=np.array(f_i_list)    
print f_i_list

delf_delta_h_list=[]    
for i in range(len(Q)) and range(len(delta_h)):
    delf_delta_h=(Dhg-Dw)*9.8*D**5*3.14**2/(32*Dw*Q[i]**2*L)
    delf_delta_h_list.append(delf_delta_h_list)
delf_delta_h_list=np.array(delf_delta_h_list)    
print delf_delta_h_list

delf_D_list=[]
for i in range(len(Q)) and range(len(delta_h)):
    delf_D=delta_h[i]*(Dhg-Dw)*9.8*5*D**4*3.14**2/(32*Dw*Q[i]**2*L)
    delf_D_list.append(delf_D_list)
delf_D_list=np.array(delf_D_list)    
print delf_D_list

delf_Q_list=[]
for i in range(len(Q)) and range(len(delta_h)):    
    delf_Q=delta_h[i]*(Dhg-Dw)*-9.8*D**5*3.14**2/(16*Dw*Q[i]**3*L)
    delf_Q_list.append(delf_Q_list)
delf_Q_list=np.array(delf_Q_list)    
print delf_Q_list

delf_L_list=[]
for i in range(len(Q)) and range(len(delta_h)):    
    delf_L=delta_h[i]*(Dhg-Dw)*-9.8*D**5*3.14**2/(32*Dw*Q[i]**2*L**2)
    delf_L_list.append(delf_L_list)
delf_L_list=np.array(delf_L_list)    
print delf_L_list


delf_i_list=[]
for i in range(len(delf_delta_h)) and range(len(delf_D)) and range(len(delf_Q)) and range(len(delf_L)):
    delf_i=(delf_delta_h**2+delf_D**2+delf_Q**2+delf_L**2)**0.5 
    delf_i_list.append(delf_i)
delf_i_list=np.array(delf_i_list)
print delf_i_list





#delf_i=(delf_delta_h**2+delf_D**2+delf_Q**2+delf_L**2)**0.5    