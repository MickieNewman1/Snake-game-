# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 12:07:03 2021
@author: mwnew
"""
# ========
#  Video Game
# Mickie Newman
# This code will create a snake game
# =========

import pygame
import random 
import time
from tkinter import messagebox

pygame.init()
pygame.mixer.init()

black = (0,0,0) 
red = (255, 0, 0)
green = (0, 255, 0)

# setting up screen 
Screen = pygame.display.set_mode((600,600))

clock = pygame.time.Clock()
snakeBlock= 10 #snake size
speed = 15 #how fast we want things to be
pygame.mixer.music.load('ding.mp3') #sound effect

# as the snake goes forward it draws a new block 
class snake:
  def __init__(self,color,screen):
    self.color = green 
    self.screen = Screen
  def snakeBody(snakeBlock, snakeList):
      """Draws a block when the snake moves forward"""
      for x in snakeList:
          pygame.draw.rect(Screen, green, [x[0],x[1], snakeBlock, snakeBlock])

class apple:
  def __init__(self,color,screen):
    self.color = color
    self.screen = screen
  def makeApple():
    """Draws apple """
    pygame.draw.rect(Screen,red,[applex,appley,snakeBlock,snakeBlock])

run = True

x1 = 300
y1 = 300
deltaX = 0 
deltaY = 0
snakeList = [] #list of x and y coordinates of the stationary blocks 
score = 1 # number of blocks in the snake

#gets the x and y coordinates for the apple is in a random place 
#  had a hard time getting rand int to work initialy so used round found on the webcite https://www.edureka.co/blog/snake-game-with-pygame/
applex = round(random.randrange(0,600 - snakeBlock)/10.0)*10.0
appley = round(random.randrange(0,600 - snakeBlock)/10.0)*10.0

snake(green,Screen)
apple(red,Screen)

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
   
    Screen.fill(black)
    #draws the apples
    apple.makeApple()
   
    # drawing the body 
    snakeHead = []
    snakeHead.append(x1) #gets the x cordinates as it goes forward 
    snakeHead.append(y1) #gets the y cordinates as it goes forward
    snakeList.append(snakeHead) # appends snakelist with x and y coordinates as its own seperate list 
    
    # as the snake goes forward it draws a new block but it needs to delete the last block 
    if len(snakeList)> score: 
        del snakeList[0]

    snake.snakeBody(snakeBlock, snakeList)
    pygame.display.update()
        
    #if the front of the snake runs into the body the game ends 
    snakeFront = snakeList[0]
    for i in range(1, score):
        if snakeFront == snakeList[i]:
            run = False
          
    #if the snake runs into the boundries  the game ends 
    if x1 >= 600 or x1 < 0 or y1 >= 600 or y1 < 0:
            run = False
    #if snake runs into the apple the score goes up by one and a new apple is spawned in a random place
    if x1 == applex and y1 == appley:
        applex = round(random.randrange(0,600 - snakeBlock)/10.0)*10.0
        appley = round(random.randrange(0,600 - snakeBlock)/10.0)*10.0
        score += 1
        pygame.mixer.music.play()
  
    clock.tick(speed)
 
#display a text window with your score when game ends
finalMessage = "You died. Your score was " + str(score - 1) + "."
messagebox.showwarning("GAME OVER", finalMessage)

pygame.quit()
quit() 