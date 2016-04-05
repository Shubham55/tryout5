# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 12:31:49 2016

@author: SHUBHAM
"""

# Illustration 11.8
# Page: 627

print'Illustration 11.8 - Page: 627\n\n'

# Solution

from scipy.optimize import fsolve

#******Data******#
rate = 0.1;# [kg/s]
conc = 3.0;# [kg vapour/100cubic m]
Density_p = 720.0;# [kg/cubic m]
Density_bed = 480.0;# [kg/cubic m]
capablity = 0.45;# [kg vapour/kg carbon]
dp = 0.0028;# [m]
time = 3.0;# [h]
#********************#

Vap_adsorbed = time*3600.0*rate;# [kg]
C_required = Vap_adsorbed*1.0/capablity;
# Two beds will be needed: one adsorbing and another regenerated.
totC_required = 2*C_required;# [kg]
print"Amount of carbon required: ",totC_required," kg\n",
Vol = (C_required/Density_bed);
# Assume:
Z = 0.5;# [m]
Area = Vol/Z;# [square m]
# From Eqn. 6.66:
T = 35.0;# [OC]
viscosity_air = 1.82*10**(-5);# [kg/m.s]
Density_air = (29/22.41)*(273.0/(T+273));
e = 1-(Density_bed/Density_p);
G = rate*(100.0/conc)*(Density_air/(Area));# [kg/square m.s]
Re = dp*G/viscosity_air;
Z = 0.5;# [m]
def f78(delta_p):
    return ((delta_p/Z)*(e**3*dp*Density_air)/((1-e)*G**2))-(150*(1-e)/Re)-1.75
delta_p = fsolve(f78,7);
print"The pressure drop is:",round(delta_p,2)," N/square m\n"
#the answers are slightly different in textbook due to approximation while here answers are precise