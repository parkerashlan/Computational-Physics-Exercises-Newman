#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 14:09:21 2019

@author: ashlan

Goal:Solve for the time it takes to travel a distance going at a relativistic
speed.
"""

x = float(input('Please input the distance in lightyears:'))
v = float(input('Please input the velocity in units of c (0.1-1.0):'))

t = x/v

propert = t*(1-v**2)**(1/2)

print('This is the time for an observer on earth:',t)
print('This is the time for a passenger on board:',propert)

