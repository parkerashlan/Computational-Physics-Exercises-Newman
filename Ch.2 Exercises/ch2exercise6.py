#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 17:14:22 2019

@author: ashlan

Goal: Calculate orbit using perihelion and the linear velocity at
perihelion
"""

import numpy as np

"""Part A: Show that v2 is the smaller root of the quadratic eqn"""

"""Don't think quadratic can be solved analytically so going to solve
numerically by using a model planet"""

#will use Earth as the model planet

M = 1.989e30 #kg
G = 6.67e-11
v1 = 30300 #m/s
l1 = 147e9 #m

a = 1
b = -(2*G*M)/(v1*l1)
c = -(v1**2-((2*G*M)/l1))

root1 = (-b+np.sqrt(b**2-(4*c)))/2
root2 = (-b-np.sqrt(b**2-(4*c)))/2

"""Root 2 is the smaller root and comes out to 29270 m/s which matches
the speed at aphelion or v2"""

"""Part B: Write a program that asks the user to enter the distance to the Sun and
velocity at perihelion, then calculates and prints the quantities l2, v2, T, and e."""

peridist = float(input("Please input the distance from the sun at perihelion:"))
perivel = float(input("Please input the velocity at perihelion:"))

#calculate v2
a = 1
b = -(2*G*M)/(perivel*peridist)
c = -(perivel**2-((2*G*M)/peridist))

v2 = (-b-np.sqrt(b**2-(4*c)))/2
l2 = (perivel*peridist)/v2

a1 = 0.5*(peridist+l2)
b1 = np.sqrt(peridist*l2)

T = (2*np.pi*a1*b1)/(peridist*perivel)

e = (l2-peridist)/(l2+peridist)

print('v2',v2,'l2',l2,'T',T,'e',e,sep='\n')



