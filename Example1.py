# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:34:25 2024

@author: mdubo
"""

import numpy as np

def distance(A, B = (0, 0), metric = 'straightline'):
    
    ''' 
    Function for computing the distance between two points.

    
    A = initial point, list. in meters.
    
    B = final point, list. in meters. default point is (0, 0)
    
    metric values:
    straightline: the shortest point between the two points, calculated using pythagorean theorem.
    taxi: calculated using only cardinal directions, if you were traveling in a taxi cab across blocks.
    '''
    
    if metric == 'straightline':
        straight_distance = np.sqrt((A[0] - B[0])**2 + (A[1]-B[1])**2);
    elif metric == 'taxi':
        straight_distance = abs(A[0] - B[0]) + abs(A[1] - B[1]);
        
    
    return straight_distance
