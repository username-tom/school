# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 14:09:02 2021

@author: tomwu
"""

import numpy as np
import matplotlib.pyplot as plt
import math
from sympy.solvers import solve
from sympy import Symbol
from scipy.optimize import curve_fit

T = [3*60+19, 3*60+19, 3*60+19, 
     3*60+34, 3*60+33, 3*60+34, 
     4*60+28, 4*60+23, 4*60+26, 
     4*60+49, 4*60+46, 4*60+48]
# =============================================================================
# rou = 998.2
# mu = 1.002
# g = 9.8
# l = 0.32
# w = 0.26
# R1 = 0.00794
# A1 = math.pi * R1
# R2 = 0.01125
# A2 = math.pi * R2
# m = w * l * 0.08 * rou
# 
# t = np.linspace(0, 0.3)
# x = Symbol('x')
# 
# h1 = 0.0121947849
# h2 = -0.22086
# h3 = 0.02768896
# c1 = 0.047065
# H = (h1*t**2 + h2*c1*t + c1**2) / h3
# 
# plt.plot(t, H)
# 
# solve((h1*x**2 + h2*c1*x + c1**2) / h3 - 0.02, x)
# x = 0.2131
# 
# L = [0.2, 0.3, 0.4, 0.6]
# 
# Q = m/T[0]/rou
# Re = rou*Q*math.pi*R1*L[0]/mu
# f = 0.0055*(1+(10**6/Re)**(1/3))
# =============================================================================

Tavg = [(T[0]+T[1]+T[2])/3, 
        (T[3]+T[4]+T[5])/3, 
        (T[6]+T[7]+T[8])/3, 
        (T[9]+T[10]+T[11])/3]
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
tubeLength = [0.20, 0.30, 0.40, 0.60]

theta = math.asin(1/150)
verticalOffset = 0.02

densityWater = 999.07 #at 15.6C
gravity = 9.81

binLength = 0.32
binWidth = 0.26
binArea = binLength * binWidth

tubeDiameter = 0.00794
tubeRadius = tubeDiameter/2
tubeArea = math.pi*math.pow(tubeRadius, 2)
TDiameter = 0.01125

mew = 0.001

deltaT = 0.001
deltaTime = []

for L in tubeLength:
    print("Length = "+str(L*100)+"cm")
    depth = 0.08
    Re = [6950]
    f = [0.014]
    v = [0]
    H = [0.1]
    i = 0
    v.append(math.sqrt(2*gravity*tubeDiameter*(H[i])/(L*(f[i]+0)+1.65*tubeDiameter)))
    Re.append(densityWater*tubeDiameter*v[i+1]/mew)
    f.append(1/((-1.8*math.log(6.9/Re[i+1]))**2))
    H.append(H[i]-(tubeArea/binArea)*v[i+1]*deltaT)
    
    while (f[i+1] - f[i]) > 0.000001:
        i=i+1
        v.append(math.sqrt(2*gravity*tubeDiameter*(H[i])/(L*(f[i]+0)+1.65*tubeDiameter)))
        Re.append(densityWater*tubeDiameter*v[i+1]/mew)
        f.append(1/((-1.8*math.log(6.9/Re[i+1]))**2))
        H.append(H[i]-(tubeArea/binArea)*v[i+1]*deltaT)
        
    
    
    friction = f[-1]
    print("Approximated f: "+str(friction))
    
    verticalTube = tubeLength[tubeLength.index(L)]*math.sin(theta)

    time = 0
    times = []
    Renolds = []
    Velocities = []
    Heights = []
    fs = []
    totalRe = 0
    countRe = 0
    
    while depth > 0:
        times.append(time)
        height = verticalTube+depth+verticalOffset
        Heights.append(depth)
    ##        velocity = math.sqrt((2*gravity*height)/(1+tubeLength*friction/tubeDiameter))
        velocity = math.sqrt((2*gravity*tubeDiameter*height)/(L*(friction+0)+1.65*tubeDiameter))
        
        Velocities.append(velocity)
        changeHeight = (tubeArea/binArea)*velocity*deltaT
        RenoyldsNumber = densityWater*tubeDiameter*velocity/mew
        Renolds.append(RenoyldsNumber)
        friction = 1/((-1.8*math.log(6.9/RenoyldsNumber))**2)
        fs.append(friction)
        totalRe += RenoyldsNumber
        countRe += 1
        depth -= changeHeight
        time += deltaT
    if countRe > 0:
        avgRe = totalRe/countRe
        
        
        timeMin = int(((time-time%60)/60))
        timeSec = int((time%60))
        print(str(timeMin)+" Min, "+str(timeSec)+" Sec")
        deltaTime.append((time-Tavg[tubeLength.index(L)])/Tavg[tubeLength.index(L)])
        print("Delta: "+str(deltaTime[-1]))
        
        print("f @ End = "+str(friction))
        print("Average Reynolds Number: "+str(avgRe))
        
        plt.plot(times, Renolds)
        plt.title('Renolds')
        plt.xlabel('Time (min)')
        plt.ylabel('Renolds Number')
        plt.show()
        
        plt.plot(times, Velocities)
        plt.title('Velocity')
        plt.xlabel('Time (min)')
        plt.ylabel('Velocity (m/s)')
        plt.show()
        
        acceleration = []
        
        for x in range(0, len(Velocities)-1):
            acceleration.append(Velocities[x+1]-Velocities[x])
        
        plt.plot(times[:len(times)-1], acceleration)
        plt.title('Acceleration')
        plt.xlabel('Time (min)')
        plt.ylabel('Acceleration (m/s^2)')
        plt.show()
        
        plt.plot(times, Heights)
        plt.title('Height')
        plt.xlabel('Time (min)')
        plt.ylabel('Height (m)')
        plt.show()
        
        print()
   
        its = list(range(1, (len(fs)+1)))
            
        plt.plot(its, fs)
        plt.title('Friction')
        plt.xlabel('Iteration')
        plt.ylabel('f')
        plt.show()
        
        plt.plot(its, Renolds)
        plt.title('Reynolds Number')
        plt.xlabel('Iteration')
        plt.ylabel('Re')
        plt.show()

        
"""
plt.plot(tubeLength, deltaTime)
plt.title('Delta Time vs Tube Length')
plt.xlabel('Length (m)')
plt.ylabel('Delta Time (sec)')
plt.show()
"""
def objective(x, a, b):
	return (a * x) + b

popt, _ = curve_fit(objective, tubeLength, deltaTime)
a, b = popt
plt.scatter(tubeLength, deltaTime)
x_line = np.linspace(min(tubeLength), max(tubeLength))
y_line = objective(x_line, a, b)
plt.plot(x_line, y_line, '--', color='red')
plt.title('Delta Time vs Tube Length')
plt.xlabel('Length (m)')
plt.ylabel('Delta Time/Ave. Time')
plt.show()

#print("Line of Best Fit: "+str(a)+" * x + "+str(b)+" * x**2 + "+str(c)+" * x**3 + "+str(d))
print("Line of Best Fit: "+str(a)+" * x + "+str(b))
print()

