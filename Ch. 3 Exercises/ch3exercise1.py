#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 10:44:49 2019

@author: ashlan

Goal: Read data from a txt file and plot it
"""

import numpy as np
import matplotlib.pyplot as plt

sunspots = np.loadtxt("./resources/sunspots.txt",float)
print(sunspots)

#Part A: Make a graph of sunspots v. time
time = sunspots[:,0]
sunspotnum = sunspots[:,1]

#Part B: Make graph with only first 1000 points
time2 = sunspots[:1001,0]
sunspotnum2 = sunspots[:1001,1]

#Part C: Plot the running average
Y = np.zeros((996,1))
time3 = sunspots[:996,0]
for i in range(5,1001):
    Y[i-5,0] = (1/10)*np.sum(sunspots[i-5:i+1,1]) 


fig,ax = plt.subplots()
#ax.plot(time,sunspotnum)
ax.plot(time3,Y)
ax.plot(time2,sunspotnum2)
plt.show()

