#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 17:35:36 2019

Last Edited:Wed Jun 19 23:09

@author: ashlan

Exercise 2.2: Altitude of a satellite
http://www-personal.umich.edu/~mejn/cp/chapters/programming.pdf
"""
import numpy as np

periods = []

for i in range(1,4):
    period = input('Please input desired period %s for satellite in s:'%i)
    periods.append(float(period))

def altitude(period):
    alt = (((6.67e-11*5.97e24*period**2)/(4*np.pi**2))**(1/3))-6371e3
    return alt

print('\nThis is the altitude for a geosynchronous orbit:',altitude(periods[0]))
print('\nThis is the altitude for a 90 min orbit:',altitude(periods[1]))
print('\nThis is the altitude for a 45 min orbit:',altitude(periods[2]))

"""The 45 min orbit would not be possible as the negative value shows that it would
need to be inside of earth"""

"""Taking into account a sidereal day is 23.93 hours the period would be 86,148 s which
results in a difference of 83m"""