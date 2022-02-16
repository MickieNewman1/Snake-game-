# -*- coding: utf-8 -*-
"""
Created on Dec  1 19:15:04 2021

@author: Mickie newman 
 debugging functions
"""

import pygame
pygame.init()

 
def boundCheck(Rect, screenSize):
    '''Returns whether a position of a Rect object is within a boundary.
    Arguments:  a Rect object 
                a 2-element screensize variable (x,y)
    Returns booleans for each edge going clockwise from top: 
        Top, Right, Bottom, Left'''
    top = True
    right = True
    bottom = True
    left = True
    
    if Rect.x >= screenSize[0]-Rect.width:
        #check to see within right boundary
        print('Right edge crossed')
        right = False
        left = True
    elif Rect.x <= Rect.width:
        #check to see within left boundary
        print('Left edge crossed')
        right = True
        left = False   
    
    if Rect.y >= screenSize[0]-Rect.height:
        #check to see within bottom boundary
        print('Bottom edge crossed')
        top = True
        bottom = False
    elif Rect.y <= Rect.height:
        #check to see within top boundary
        print('Top edge crossed')
        top = False
        bottom = True

    return not top, not right, not bottom, not left

##Test function
#rect.x = 500
#print(boundCheck(rect,size))
#
#rect.y = -10
#print(boundCheck(rect,size))