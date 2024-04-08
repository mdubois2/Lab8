# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 11:21:07 2024

@author: mdubo
"""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

x_step = rng.random(500); #Creates a set of 500 random numbers from 0 to 1 for each array
y_step = rng.random(500);
z_step = rng.random(500);

x_step = x_step > 0.5; #Converts these arrays to a series of 0s and 1s
y_step = y_step > 0.5;
z_step = z_step > 0.5;

x_step = 2*(((2*x_step + 1)/2) - 1) #Converts the 0s and 1s to -1s and 1s
y_step = 2*(((2*y_step + 1)/2) - 1)
z_step = 2*(((2*z_step + 1)/2) - 1)

x_dist = np.cumsum(x_step) #Takes the cumulative sum of each array
y_dist = np.cumsum(y_step)
z_dist = np.cumsum(z_step)

plt.figure(figsize=(20, 10)) #Plots it all
ax = plt.axes(projection='3d') #Allows for 3d plotting
ax.plot(x_dist, y_dist, z_dist)
ax.plot(x_dist[0], y_dist[0], z_dist[0], 'r+')
ax.plot(x_dist[-1], y_dist[-1], z_dist[-1], 'b+')
ax.set_box_aspect(aspect=None, zoom=0.93) #Makes plot smaller on screen, z axis title doesn't get pushed off screen anymore
ax.legend(['Position of Object', 'Starting Point', 'Ending Point']);
ax.set_xlabel('Position in x Direction')
ax.set_ylabel('Postition in y Direction')
ax.set_zlabel('Position in z Direction')
ax.set_title('Randomly Generated 3D Movement of an Object')

