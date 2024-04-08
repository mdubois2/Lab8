# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:08:54 2024

@author: mdubo
"""

import numpy as np

rng = np.random.default_rng() #Creates rng seed

samples = rng.random(100) #Creates list of 100 random numbers from 0 to 1

flips = (samples > 0.5) #Sorts these numbers into true or false 

heads = np.sum(flips) #Amount of heads is the amount of samples that were above 0.5
tails = 100 - np.sum(flips) #Amount of samples under 0.5

print(heads, tails);

