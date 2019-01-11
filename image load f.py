# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 17:08:57 2019

@author: sg00898
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pandas as pd


img=mpimg.imread('hi.png')
plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
plt.imshow(img)
    