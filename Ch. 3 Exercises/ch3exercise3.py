#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 22:09:24 2019

@author: ashlan
"""

import numpy as np
import pylab as py

stm = np.loadtxt('./resources/stm.txt',float)

py.imshow(stm,origin="lower", extent = [0,10,0,10])

py.show()

