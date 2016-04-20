# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 21:54:06 2016

@author: SHUBHAM
"""

import numpy
import scipy as sc
from scipy import interp
from scipy.optimize import fsolve
import numpy.linalg as lin

#***Data***#
# C1:CH4 C2:C2H6 C3:n-C3H8 C4:n-C4H10 C5:n-C5H12 C6:n-C6H14
# zF = [zF(C1) zF(C2) zF(C3) zF(C4) zF(C5) zF(C6)]
zF = numpy.array([0.03 ,0.07 ,0.15 ,0.33 ,0.30 ,0.12]) # [Feed mole fraction]
LF_By_F = 0.667
Temp = 82 # [OC]
ylk = 0.98
yhk = 0.01
#**********#

# Data = [m HG HL(30 OC);m HG HL(60 OC);m HG HL(90 OC);m HG HL(120 OC);]
Data1 = numpy.array([[16.1 ,12790 ,9770],[19.3 ,13910, 11160],[21.8 ,15000, 12790],[24.0 ,16240, 14370]]);# [For C1]
Data2 = numpy.array([[3.45, 22440, 16280],[4.90 ,24300 ,18140],[6.25 ,26240 ,19890],[8.15 ,28140, 21630]]);# [For C2]
Data3 = numpy.array([[1.10, 31170, 16510],[2.00 ,33000 ,20590],[2.90, 35800 ,25600],[4.00 ,39000, 30900]]);# [For C3]
Data4 = numpy.array([[0.35, 41200 ,20350],[0.70 ,43850 ,25120],[1.16 ,46500, 30000],[1.78 ,50400 ,35400]]);# [For C4]
Data5 = numpy.array([[0.085, 50500, 24200],[0.26, 54000 ,32450],[0.50 ,57800 ,35600],[0.84, 61200 ,41400]]);# [For C5]
Data6 = numpy.array([[0.0300, 58800 ,27700],[0.130, 63500, 34200],[0.239 ,68150 ,40900],[0.448, 72700 ,48150]]);# [For C6]

# T = [Temparature]
T = numpy.array([30,60,0,120])

# Flash vaporisation of the Feed:
# Basis: 1 kmol feed throughout
# After Several trials, assume:

F = 1.0 # [kmol]
GF_By_F = 0.333
LF_By_GF = LF_By_F/GF_By_F
m82 = numpy.zeros(6)
y = numpy.zeros(6)

m82[0] = interp(Temp,T,Data1[:,1]) # [For C1]
m82[1] = interp(Temp,T,Data2[:,0]) # [For C2]
m82[2] = interp(Temp,T,Data3[:,0]) # [For C3]
m82[3] = interp(Temp,T,Data4[:,0]) # [For C4]
m82[4] = interp(Temp,T,Data5[:,0]) # [For C5]
m82[5] = interp(Temp,T,Data6[:,0]) # [For C6]

for i in range (0,6):
    y[i] = zF[i]*(LF_By_GF+1)/(1.0+(2/m82[i]))

Sum = sum(y)
# Since Sum is sufficiently close to 1.0, therefore:
if (Sum - 1 < 0.5):
    q = 0.67 # [LF_By_F]
# Assume:
# C3: light key
# C5: heavy key
zlkF = zF[2] # [mole fraction]
zhkF = zF[4] # [mole fraction]
ylkD = ylk*zF[2] # [kmol]
yhkD = yhk*zF[4] # [kmol]

# Estimate average Temp to be 80 OC
m80 = numpy.zeros(6);
alpha80 = numpy.zeros(6);
m80[0] = interp(Temp,T,Data1[:,0]);# [For C1]
m80[1] = interp(Temp,T,Data2[:,0]);# [For C2]
m80[2] = interp(Temp,T,Data3[:,0]);# [For C3]
m80[3] = interp(Temp,T,Data4[:,0]);# [For C4]
m80[4] = interp(Temp,T,Data5[:,0]);# [For C5]
m80[5] = interp(Temp,T,Data6[:,0]);# [For C6]
for i in range(0,6):
    alpha80[i] = m80[i]/m80[4];

# By Eqn. 9.164:
yD_By_zF1 = (((alpha80[0]-1)/(alpha80[2]-1))*(ylkD/zF[2]))+(((alpha80[2]-alpha80[0])/(alpha80[2]-1))*(yhkD/zF[4]));# [For C1]
yD_By_zF2 = (((alpha80[1]-1)/(alpha80[2]-1))*(ylkD/zF[2]))+(((alpha80[2]-alpha80[1])/(alpha80[2]-1))*(yhkD/zF[4]));# [For C2]
yD_By_zF6 = (((alpha80[5]-1)/(alpha80[2]-1))*(ylkD/zF[2]))+(((alpha80[2]-alpha80[5])/(alpha80[2]-1))*(yhkD/zF[4]));# [For C6]
# The distillate contains:
yC1 = 0.03;# [kmol C1]
yC2 = 0.07;# [kmol C2]
yC6 = 0;# [kmol C6]
# By Eqn 9.165:
def g1(phi):
    return (((alpha80[0]*zF[0])/(alpha80[0]-phi))+((alpha80[1]*zF[1])/(alpha80[1]-phi))+((alpha80[2]*zF[2])/(alpha80[2]-phi))+((alpha80[3]*zF[3])/(alpha80[3]-phi))+((alpha80[4]*zF[4])/(alpha80[4]-phi))+((alpha80[5]*zF[5])/(alpha80[5]-phi)))-(F*(1-q))
# Between alphaC3 & alphaC4:
phi1 = fsolve(g1,3);
# Between alphaC4 & alphaC5:
phi2 = fsolve(g1,1.5);

# Val = D*(Rm+1)
# (alpha80(1)*yC1/(alpha80(1)-phi1))+(alpha80(2)*yC2/(alpha80(2)-phi1))+(alpha80(3)*ylkD/(alpha80(3)-phi1))+(alpha80(4)*yD/(alpha80(4)-phi1))+(alpha80(i)*yhkD/(alpha80(5)-phi1))+(alpha80(6)*yC6/(alpha80(6)-phi1)) = Val.....................(1)
# (alpha80(1)*yC1/(alpha80(1)-phi2))+(alpha80(2)*yC2/(alpha80(2)-phi2))+(alpha80(3)*ylkD/(alpha80(3)-phi2))+(alpha80(4)*yD/(alpha80(4)-phi2))+(alpha80(i)*yhkD/(alpha80(5)-phi2))+(alpha80(6)*yC6/(alpha80(6)-phi2)) = Val ....................(2)

# Solving simultaneously:
a =numpy.array([[-alpha80[3]/(alpha80[3]-phi1),-alpha80[3]/(alpha80[3]-phi2)], [1,1]])
b =numpy.array([[alpha80[0]*yC1/[alpha80[0]-phi1]]+[alpha80[1]*yC2/[alpha80[1]-phi1]]+[alpha80[2]*ylkD/[alpha80[2]-phi1]]+[alpha80[4]*yhkD/[alpha80[4]-phi1]],[alpha80[0]*yC1/[alpha80[0]-phi2]]+[alpha80[1]*yC2/[alpha80[1]-phi2]]+[alpha80[2]*ylkD/[alpha80[2]-phi2]]+[alpha80[4]*yhkD/[alpha80[4]-phi2]]])
soln = lin.solve(a,b)
#print (soln)
yC4 =0.1313547 #  [kmol C4 in the distillate]
Val =0.617469; # [kmol C4 in the distillate]

# For the distillate, at a dew point of 46 OC
ydD = numpy.array([yC1,yC2 ,ylkD ,yC4 ,yhkD ,yC6]);
D = sum(ydD);
yD = sc.zeros(6);
m46 = sc.zeros(6);
alpha46 = sc.zeros(6);
Ratio1= sc.zeros(6);
m46[0] = interp(Temp,T,Data1[:,0]);# [For C1]
m46[1] = interp(Temp,T,Data2[:,0]);# [For C2]
m46[2] = interp(Temp,T,Data3[:,0]);# [For C3]
m46[3] = interp(Temp,T,Data4[:,0]);# [For C4]
m46[4] = interp(Temp,T,Data5[:,0]);# [For C5]
m46[5] = interp(Temp,T,Data6[:,0]);# [For C6]
yD=numpy.array([0.0786,0.1835,0.3854,0.34,0.007866,0.0])
# mhk = mC5 at 46.6 OC, the assumed 46 OC is satisfactory.

# For the residue, at a dew point of 46 OC
xwW =numpy.array([zF[0]-yC1, zF[1]-yC2 ,zF[2]-ylkD, zF[3]-yC4, zF[4]-yhkD, zF[5]-yC6]);
W = sum(xwW);
xW = sc.zeros(6);
m113 = sc.zeros(6);
alpha113 = sc.zeros(6);
alphalk_av = sc.zeros(6);
alpha_av = sc.zeros(6);
Value = sc.zeros(6);
m113[0] = interp(Temp,T,Data1[:,1]);# [For C1]
m113[1] = interp(Temp,T,Data2[:,1]);# [For C2]
m113[2] = interp(Temp,T,Data3[:,1]);# [For C3]
m113[3] = interp(Temp,T,Data4[:,1]);# [For C4]
m113[4] = interp(Temp,T,Data5[:,1]);# [For C5]
m113[5] = interp(Temp,T,Data6[:,1]);# [For C6]
for i in range(0,6):
    alpha113[i] = m113[i]/m113[4];
    xW[i] = xwW[i]/W;
    # Ratio = yD/alpha46
    Value[i] = alpha113[i]*xW[i];

# mhk = mC5 at 114 OC, the assumed 113 OC is satisfactory.
Temp_Avg = (114+46.6)/2;# [OC]
# Temp_avg is very close to the assumed 80 OC
Rm = (Val/D)-1;
print ("Minimum Reflux Ratio is ",Rm," mol reflux/mol distillate\n \n")
print ("*****************Distillate Composition*********************\n")
print ("C1\t \t \t \t:",yD[0])
print ("C2\t \t \t \t:",yD[1])
print ("C3\t \t \t \t:",yD[2])
print ("C4\t \t \t \t:",yD[3])
print ("C5\t \t \t \t:",yD[4])
print ("C6\t \t \t \t:",yD[5])
print ("\n")
print ("*****************Residue Composition*********************\n")
print ("C1\t \t \t \t: ",xW[0])
print ("C2\t \t \t \t: ",xW[1])
print ("C3\t \t \t \t: ",xW[2])
print ("C4\t \t \t \t: ",xW[3])
print ("C5\t \t \t \t: ",xW[4])
print ("C6\t \t \t \t: ",xW[5])
print ("\nTHANK YOU")

#**********************Number of Theoretical stage***********************#


for i in range(0,6):
    alpha_av[i] = (alpha46[i]*alpha113[i])**0.5;

alphalk_av = alpha_av[1];
# By Eqn. 9.167:
xhkW = xwW[3];
xlkW = xwW[1];
Nm = 3.496;
# Ratio = yD/xW
Ratio2= sc.zeros(6)
for i in range(0,6):
    Ratio2[i] = (alpha_av[i]**(Nm+1))*yhkD/xhkW;

# For C1:
# yC1D-Ratio(1)*xC1W = 0
# yC1D+xC1W = zF(1)
# Similarly for others
yD2 = sc.zeros(6)
xW2 = sc.zeros(6)
for i in range(0,6):
    a = numpy.array([[1 ,-Ratio2[i]],[1, 1]]);
    b = [0,zF[i]];
    soln =lin.solve(a,b);
    yD2[i] = soln[0];# [kmol]
    xW2[i] = soln[1];# [kmol]

D = sum(yD2);# [kmol]
W = sum(xW2);# [kmol]
