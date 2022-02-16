# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 12:07:03 2021

@author: mwnew
"""

import pygame
import random 
import time



pygame.init()


white = (255, 255, 255)
black = (0,0,0)

# setting up screen 
Screen = pygame.display.set_mode((600,600))

clock = pygame.time.Clock()
block= 10
speed = 15


# as the snake goes forward it draws a new block 
def snakeBody(snakeBlock, snakeList):
    """Dras a block when the snake moves forward"""
    for x in snakeList: # for all the coordinates in the snake list draw a block
        pygame.draw.rect(Screen, black, [x[0],x[1], block, block])
        



run = True
#starting position and front of the snake
x1 = 300
y1 = 300

deltaX = 0 
deltaY = 0

snakeList = [] #list of x and y coordinates of the stationary blocks 
score = 1 # number of blocks in the snake

#gets the x and y coordinates for the apple is in a random place 
# for the longest time couldnt get just randint to work for spawning the apples untill I saw round used on https://www.edureka.co/blog/snake-game-with-pygame/
applex = round(random.randrange(0,600 - block)/10.0)*10.0
appley = round(random.randrange(0,600 - block)/10.0)*10.0

# game loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # Keys for moving the snake 
        if event.type == pygame.KEYDOWN:
            #pressing the up arrow key makes the snake go up
            if event.key == pygame.K_UP:
                deltaX = 0
                deltaY = -10
            #pressing the down arrow key makes the snake go down 
            elif event.key == pygame.K_DOWN:
                deltaX = 0
                deltaY= 10
            #presing the left arrow key makes the snake go left
            elif event.key == pygame.K_LEFT:
                deltaX = -10
                deltaY = 0
            #pressing the right arrow key makes the snake go right  
            elif event.key == pygame.K_RIGHT:
                deltaX = 10
                deltaY = 0
                
     #changes x and y position based on i          
    x1 += deltaX
    y1 += deltaY
   
    Screen.fill(white)
    
    #draws the apples
    pygame.draw.rect(Screen,black, [applex,appley,block,block])
   
    
    # getting the coordinates for the blocks 
    snakeFront = []
    snakeFront.append(x1) #gets the x cordinates as it goes forward 
    snakeFront.append(y1) #gets the y cordinates as it goes forward
    snakeList.append(snakeFront) # appends snakelist with x and y coordinates as its own seperate list 
    
    # as the snake goes forward it draws a new block but it needs to delete the last block 
    if len(snakeList)> score: 
        del snakeList[0]
        
        
    snakeBody(block, snakeList)
    pygame.display.update()
    
    
    #if the fron of the snake runs into the body the game ends 
    snakeHead = snakeList[0]
    for i in range(1, score):
        if snakeHead == snakeList[i]:
            run = False
          
    #if the snake runs into the boundries  the game ends 
    if x1 >= 600 or x1 < 0 or y1 >= 600 or y1 < 0:
            run = False
            
            
    #if snake runs into the apple the score goes up by one and a new apple is spawned in a random place
    if x1 == applex and y1 == appley:
        applex = round(random.randrange(0,600 - block)/10.0)*10.0
        appley = round(random.randrange(0,600 - block)/10.0)*10.0
        score += 1
    
    clock.tick(speed)
 
pygame.quit()
quit()
 
 


