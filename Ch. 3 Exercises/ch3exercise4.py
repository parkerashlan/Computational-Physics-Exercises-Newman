#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 15:48:35 2019

@author: ashlan
"""
import vpython as v
import numpy as np
L = 2
R = 0.3

#Part A
for i in range(-L,L+1):
    for j in range(-L,L+1):
        for k in range(-L,L+1):
            v.sphere(pos = v.vector(i,j,k),radius = R,color = v.color.magenta)
            if i%2 == 0:
                if k%2 == 0 and j%2 == 0:
                    v.sphere(pos = v.vector(i,j,k),radius = R,color = v.color.blue)
                if k%2 != 0 and j%2 != 0:
                    v.sphere(pos = v.vector(i,j,k),radius = R,color = v.color.blue)
            else:
                if k%2 == 0 and j%2 != 0:
                    v.sphere(pos = v.vector(i,j,k),radius = R,color = v.color.blue)
                if k%2 != 0 and j%2 == 0:
                    v.sphere(pos = v.vector(i,j,k),radius = R,color = v.color.blue)
                    

#Part B
fcc = np.arange(-L,L,0.5)
index = []

for g in range(0,len(fcc),2):
    index.append(g)

fccnew = np.delete(fcc,index)

for l in fccnew:
    for m in fccnew:
        for n in fccnew:
            v.sphere(pos = v.vector(l,m,n),radius = 0.3,color = v.color.magenta)