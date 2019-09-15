#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 15:11:41 2019

@author: ashlan

Goal:Graph different functions
"""

import numpy as np
import matplotlib.pyplot as plt

#Deltoid Curve
theta = np.linspace(0,2*np.pi)

x = 2*np.cos(theta)+np.cos(2*theta)
y = 2*np.sin(theta) - np.sin(2*theta)


#plt.plot(x,y)
#plt.show()

#Galilean Spiral
theta2 = np.linspace(0,10*np.pi,100)

x2 = (theta2**2)*np.cos(theta2)
y2 = (theta2**2)*np.sin(theta2)

#plt.plot(x2,y2)
#plt.show()

#Fey's Function
theta3 = np.linspace(0,24*np.pi,10000)

r = np.e**(np.cos(theta3)) - 2*np.cos(4*theta3) + np.sin(theta3/12)**5

x3 = r*np.cos(theta3)
y3 = r*np.sin(theta3)

#plt.plot(x3,y3)
#plt.show()