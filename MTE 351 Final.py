# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 19:01:47 2020

@author: tomwu
"""

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

Vs = 6
Vs_1 = 9
Vs_2 = 12
alpha = 0.3
k = 4
k_1 = 8
k_2 = 12
A = 5
L = 10
c4 = k*A/L
c4_1 = k_1*A/L
c4_2 = k_2*A/L
R5 = 50
R5_1 = 100
R5_2 = 200
thetaA = 25+273
delta = 0.01
tplot = np.linspace(0, Vs/delta)
tcool = np.linspace(Vs/delta, Vs/delta+500)
tplot_1 = np.linspace(0, Vs/delta)
tcool_1 = np.linspace(Vs/delta, Vs/delta+500)
tplot_2 = np.linspace(0, Vs/delta)
tcool_2 = np.linspace(Vs/delta, Vs/delta+500)

def model(theta, t):
    if (t>Vs/delta):
        dthetadt = -1/c4/R5*theta + 1/c4/R5*thetaA
    else:
        dthetadt = -1/c4/R5*theta + alpha/c4*(Vs-delta*t)*(Vs-delta*t)/(10000+0.001*t*t)*t + 1/c4/R5*thetaA
    return dthetadt

#def model_1(theta, t):
#    if (t>Vs_1/delta):
#        dthetadt = -1/c4/R5*theta + 1/c4/R5*thetaA
#    else:
#        dthetadt = -1/c4/R5*theta + alpha/c4_1*(Vs_1-delta*t)*(Vs_1-delta*t)/(10000+0.001*t*t)*t + 1/c4/R5*thetaA
#    return dthetadt
#
#def model_2(theta, t):
#    if (t>Vs_2/delta):
#        dthetadt = -1/c4/R5*theta + 1/c4/R5*thetaA
#    else:
#        dthetadt = -1/c4/R5*theta + alpha/c4*(Vs_2-delta*t)*(Vs_2-delta*t)/(10000+0.001*t*t)*t + 1/c4/R5*thetaA
#    return dthetadt


#def model_1(theta, t):
#    if (t>Vs/delta):
#        dthetadt = -1/c4_1/R5*theta + 1/c4_1/R5*thetaA
#    else:
#        dthetadt = -1/c4_1/R5*theta + alpha/c4_1*(Vs-delta*t)*(Vs-delta*t)/(10000+0.001*t*t)*t + 1/c4_1/R5*thetaA
#    return dthetadt
#
#def model_2(theta, t):
#    if (t>Vs/delta):
#        dthetadt = -1/c4_2/R5*theta + 1/c4_2/R5*thetaA
#    else:
#        dthetadt = -1/c4_2/R5*theta + alpha/c4_2*(Vs-delta*t)*(Vs-delta*t)/(10000+0.001*t*t)*t + 1/c4_2/R5*thetaA
#    return dthetadt

def model_1(theta, t):
    if (t>Vs/delta):
        dthetadt = -1/c4/R5_1*theta + 1/c4/R5_1*thetaA
    else:
        dthetadt = -1/c4/R5_1*theta + alpha/c4*(Vs-delta*t)*(Vs-delta*t)/(10000+0.001*t*t)*t + 1/c4/R5_1*thetaA
    return dthetadt

def model_2(theta, t):
    if (t>Vs/delta):
        dthetadt = -1/c4/R5_2*theta + 1/c4/R5_2*thetaA
    else:
        dthetadt = -1/c4/R5_2*theta + alpha/c4*(Vs-delta*t)*(Vs-delta*t)/(10000+0.001*t*t)*t + 1/c4/R5_2*thetaA
    return dthetadt


theta = odeint(model, 25+273, tplot)
theta_cool = odeint(model, theta[49], tcool)
theta_1 = odeint(model_1, 25+273, tplot_1)
theta_cool_1 = odeint(model_1, theta_1[49], tcool_1)
theta_2 = odeint(model_2, 25+273, tplot_2)
theta_cool_2 = odeint(model_2, theta_2[49], tcool_2)

#plt.plot(tplot, theta, 'r-', label='Heating @ 6V')
#plt.plot(tcool, theta_cool, 'b-', label='Cooling @ 6V')
#plt.plot(tplot_1, theta_1, 'r--', label='Heating @ 9V')
#plt.plot(tcool_1, theta_cool_1, 'b--', label='Cooling @ 9V')
#plt.plot(tplot_2, theta_2, 'r.', label='Heating @ 12V')
#plt.plot(tcool_2, theta_cool_2, 'b.', label='Cooling @ 12V')
#plt.plot(tplot, theta, 'r-', label='Heating @ k = 4')
#plt.plot(tcool, theta_cool, 'b-', label='Cooling @ k = 4')
#plt.plot(tplot_1, theta_1, 'r--', label='Heating @ k = 8')
#plt.plot(tcool_1, theta_cool_1, 'b--', label='Cooling @ k = 8')
#plt.plot(tplot_2, theta_2, 'r.', label='Heating @ k = 12')
#plt.plot(tcool_2, theta_cool_2, 'b.', label='Cooling @ k = 12')
plt.plot(tplot, theta, 'r-', label='Heating @ R5 = 50')
plt.plot(tcool, theta_cool, 'b-', label='Cooling @ R5 = 50')
plt.plot(tplot_1, theta_1, 'r--', label='Heating @ R5 = 100')
plt.plot(tcool_1, theta_cool_1, 'b--', label='Cooling @ R5 = 100')
plt.plot(tplot_2, theta_2, 'r.', label='Heating @ R5 = 200')
plt.plot(tcool_2, theta_cool_2, 'b.', label='Cooling @ R5 = 200')
plt.xlabel('Time(second)')
plt.ylabel('Temperature(K)')
plt.legend()
plt.show()