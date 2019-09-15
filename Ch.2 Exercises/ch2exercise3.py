#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 00:57:15 2019

@author: ashlan

Exercise 2.3: Calculate the corresponding polar coordinates from a set of 
Cartesian coordinates.
"""

import numpy as np

coords = input('Please input x and y coordinate in the form x,y:')
coords = coords.split(',')
coords[0] = float(coords[0])
coords[1] = float(coords[1])

r = coords[0]**2+coords[1]**2
theta = np.arctan(coords[1]/coords[0])
theta = np.rad2deg(theta)

print(r,theta)