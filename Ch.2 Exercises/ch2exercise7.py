#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 15:40:50 2019

@author: ashlan

Goal: Write all Catalan numbers less than or equal to one billion
"""

c0 = 1
cn = c0
cn1 = 0
n = 0
catnumb = []

while cn1 < 1e9:
    
    cn1 = ((4*n+2)*cn)/(n+2)
    catnumb.append(cn1)
    
    cn = catnumb[n]
    n = n+1
    
print(catnumb)
    