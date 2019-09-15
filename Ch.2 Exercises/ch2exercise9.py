#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 11:54:06 2019

@author: ashlan

Goal: Calculate Madelung Constant
"""
import numpy as np

#set number of atoms
x = np.arange(-100,100)
y = np.arange(-100,100)
z = np.arange(-100,100)

#create a "lattice" using meshgrid because it makes a grid of points according
#to the parameters 
X,Y,Z = np.meshgrid(x,y,z)

#Evaluate the sums simultaneously
M = ((-1.0)**(X+Y+Z))/np.sqrt(X**2+Y**2+Z**2)

#Set X=Y=Z=0 to 0
M[100,100,100] = 0

const = M.sum()
print(const)