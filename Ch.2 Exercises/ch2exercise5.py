#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 14:44:50 2019

@author: ashlan

Goal: Find the transmission and reflection probabilities.
"""

import numpy as np

m = 9.11e-31 #kg
E = 10 #eV
hbar = 6.582e-16 #eV*s
V = 9 #eV


k1 = np.sqrt(2*m*E)/hbar
k2 = np.sqrt(2*m*(E-V))/hbar

T = (4*k1*k2)/(k1+k2)**2
R = ((k1-k2)/(k1+k2))**2

print('This is the transmission probability:',T)
print('This is the reflection probabilty:',R)