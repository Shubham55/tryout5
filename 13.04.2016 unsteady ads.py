# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 12:25:48 2016

@author: SHUBHAM
"""




#import matplotlib
#import scipy
import numpy
import matplotlib.pyplot as plt

#%matplotlib inline
# Solution

#*****Data******#
Yo = 0.00267;# [kg H2O/kg dry air]
Yb = 0.0001;# [kg H2O/kg dry air]
Ye = 0.024;# [kg H2O/kg dry air]
Z = 0.61;# [m]
G_prime = 0.1295;# [kg/square m.s]
#******************#

# The equilicrium data is plotted in Fig. 11.45 (Pg 637)
# The gel is initially "dry" and the effluent air initially of so low a humidity asto be substantially dry, so that the operating line passes through the origin of the figure
# The operating line is then drawn to intersect the equilibrium curve.
# Data = [Y[kg H2O/kg dry air] Y_star[kg H2O/kg dry air]]
Data =numpy.array([[0.0001, 0.00003],[0.0002, 0.00007],[0.0004 ,0.00016],[0.0006, 0.00027],[0.0008, 0.00041],[0.0010, 0.00057],[0.0012 ,0.000765],[0.0014, 0.000995],[0.0016, 0.00123],[0.0018 ,0.00148],[0.0020 ,0.00175],[0.0022 ,0.00203],[0.0024 ,0.00230]])
Val1 = numpy.zeros(13);
# Val1 = [1/(Y-Y_star)]
for i in range(0,13):
    Val1[i] = 1/(Data[i,0]-Data[i,1]);

# Graphical Integration:
plt.plot(Data[:,0],Val1);
plt.grid('on');
plt.xlabel("Y(kg H20 / kg dry air)");
plt.ylabel("1 / (Y-Y_star)");
plt.title("Graphical Integration");
plt.show()
# Area under The curve between Y = Yb and Y = Y:
Area = [0 ,0.100 ,2.219 ,2.930 ,3.487 ,3.976 ,4.438 ,4.915, 5.432, 6.015, 6.728 ,7.716 ,9.304];
# The total number of transfer unit corresponding to adsorption zone:
NtoG = 9.304;
Val2 = numpy.zeros(13);
Val3 = numpy.zeros(13);
# Val2 = [(w-wb)/wo]
# Val3 = [Y/Yo]
for i in range(0,13):
    Val2[i] = Area[i]/NtoG;
    Val3[i] = Data[i,0]/Yo;

# Eqn. 11.74 can be arranged as follows:
#f = scipy.integrate((1-(Y/Yo)),(w-wb)/wa,0,1)

plt.plot(Val2,Val3);
plt.grid('on');
plt.xlabel("(w-wb) / wo");
plt.ylabel("Y / Yo");
plt.title("Break through curve");
plt.show()
# From area above the curve of scf(2):
f = 0.530;

Gs = G_prime;# [kg/square m.s]
# From Illustration: 11.6
kYap = 31.6*G_prime**0.55;# [kg H2O/cubic m s delta_Y]
kSap = 0.965;# [kg H2O/cubic m s delta_X]
# From Fig. 11.48:
Xt = 0.0858;# [kg H2O/kg gel]
# From Eqn. 11.76:
Ss = Yo*Gs/Xt;# [kg/square m.s]
m = 0.0185;# [average slope of equilibrium curve]
# From Eqn. 11.51 & Eqn. 11.52:
HtG = Gs/kYap;# [m]
HtS = Ss/kSap;# [m]
HtoG = HtG+(m*Gs/Ss)*HtS;# [m]
# From Eqn. 11.79:
Za = NtoG*HtoG;# [m]
# From Eqn. 11.74:
Degree = (Z-(f*Za))/Z;
Density_bed = 671.2;# [Illustration 11.6, kg/cubic m]
mass_gel = Z*Density_bed;# [kg/square m]
# At saturation point the gel contins:
Y1 = mass_gel*Degree*Xt;# [kg H2O/square m cross section]
# The air introduces:
Y2 = Gs*Yo;# [kg/square m s]
print"Time to reach breakpoint is: ",round((Y1/(Y2*3600)),4)," h\n"