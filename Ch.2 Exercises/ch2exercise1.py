#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 16:38:44 2019

Last Edited: Wed Jun 19 23:09

@author: ashlan

Exercise 2.1: Another ball dropped from a tower

Computational Physics by Mark Newman
http://www-personal.umich.edu/~mejn/cp/exercises.html

Goal:Take user input for for height and print the time it takes to hit the ground
"""
import math as m

height = input('Please input height in m:')

y = float(height)
a = -9.8
t=0.
vy=0.
tcalc = m.sqrt(y/(9.8*0.5))

while y>=0:
    vy += a
    y += vy
    t += 1
 

print(tcalc)
print(t)
    
    