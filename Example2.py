# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:25:13 2024

@author: mdubo
"""

'''
Function that rotates a vector using the rotation matrix

vector: list, tuple, or array of the components of the vector (x component, y component)
theta: the angle that you want to rotate your vector by
'''


import numpy as np

def rotate(vector, theta):
    
    rotation_matrix = np.array([[np.cos(theta*np.pi/180), -np.sin(theta*np.pi/180)],[np.sin(theta*np.pi/180), np.cos(theta*np.pi/180)]]);
    
    vector_rot = np.matmul(rotation_matrix, (np.array([vector[0], vector[1]])));
    
    return vector_rot

x_rot, y_rot = rotate(np.array([3, 4]), 90);



