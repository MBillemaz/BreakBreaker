 #!/usr/bin/env python 
# -*- coding: utf-8 -*-
import pygame
import constante
import game
from pygame.locals import *
from time import*
from threading import Timer
pygame.init()

WINDOW_X = 640
WINDOW_Y = 480
windows =  pygame.display.set_mode((WINDOW_X, WINDOW_Y))

class brick():
    pic = pygame.image.load("./Sprites/Brick/block.png").convert_alpha()
    posX = None
    posY = None
    isDead = False

class Point():
    x=None
    y=None
    
background = pygame.image.load("./Sprites/background/background.jpg")
abscisse_fond = 0
windows.blit(background, (0,0))
yp = 430
xp = 320
pygame.key.set_repeat(5,5)
font = pygame.font.Font("GearsOfPeace.ttf",36)
title = font.render("BreakBreaker",1,(255,255,255))
begin = font.render("Begin : Space",1,(255,255,255))
help = font.render("Help : H",1,(255,255,255))
left = pygame.image.load("left.jpg").convert_alpha()
right = pygame.image.load("right.jpg").convert_alpha()
control = font.render("Move right     left", 1, (255,255,255))
action = font.render("Action",1, (255,255,255))
spacebar = pygame.image.load("Espace.png").convert_alpha()
win = font.render("You win ! o/ o/ \o \o", 1 , (255,255,255))
lose = font.render("You lose... :'(", 1 , (255,255,255))       
retry = font.render("Do you want replay ? Y/N", 1 , (255,255,255))

POSPAD_Y = 420
taillePad = 125
speed= Point()
speed.x = 3
speed.y = 3
ball = Point()
ballSprite = pygame.image.load("Sprites/ball/ball.png")

player = pygame.image.load("./Sprites/Paddle/paddle.png").convert_alpha()

liste = []

##brick1 = brick()
##brick2 = brick()
##brick3 = brick()
##brick4 = brick()
##brick5 = brick()
##brick6 = brick()
##brick7 = brick()
##brick8 = brick()
##brick9 = brick()
##brick10 = brick()

def menu():
    windows.blit(background,(0,0))
    windows.blit(title, (200,50))
    windows.blit(begin, (50,350))
    windows.blit(help, (50,400))
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                constante.menu = False
                constante.play = True
                brick_gen()
                initBall()
            if event.key == K_h:
                constante.menu = False
                constante.helpmenu = True
                
            
def help_menu():
    windows.blit(background,(0,0))
    windows.blit(control,(50,200))
    windows.blit(left, (150,250))
    windows.blit(right, (300,250))
    windows.blit(action, (50, 400))
    windows.blit(spacebar, (200, 400))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT or event.key == K_ESCAPE:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                constante.menu = True
                constante.helpmenu = False
    
def place():
    posPad = 0

    
    brick1.posX = 20
    brick1.posY = 20

    brick2.posX = 65
    brick2.posY = 20
    
    brick3.posX = 110
    brick3.posY = 20

    brick4.posX = 155
    brick4.posY = 20

    brick5.posX = 200
    brick5.posY = 20

    brick6.posX = 245
    brick6.posY = 20

    brick7.posX = 290
    brick7.posY = 20

    brick8.posX = 335
    brick8.posY = 20

    brick9.posX = 380
    brick9.posY = 20
    
    brick10.posX = 425
    brick10.posY = 20

def initBall():

    window = pygame.display.set_mode((WINDOW_X, WINDOW_Y))

    #Get the middle of the window
    ball.x = WINDOW_X/2
    ball.y = WINDOW_Y/2

def brick_gen():
    posX = 20
    posY = 20
    
    for i in range (0,104):
        testbrick = brick()
        testbrick.posX = posX
        testbrick.posY = posY
        liste.append(testbrick)
        print i
        if posX >= 560:
            posX = 20
            posY = posY + 15
        else:
            posX = posX + 45
        
                         
def updateBall():
    #update the position of the ball
    ball.x += speed.x
    ball.y += speed.y

    #update the position of the sprite of the ball
    windows.blit(ballSprite,(ball.x, ball.y))
    collision()



    
def collision():
    #Ball and window 
    #If the ball is at the left or right of window -> reverse the speedX
    if ball.x <=0 or ball.x >= WINDOW_X - 16:
        speed.x = -1*speed.x

            #If the ball is at the top of window -> reverse the speedY
    if ball.y <= 0:
        speed.y = -1*speed.y
        
    #Ball and Paddle
            #The Ball is on the paddle
    if ball.y >= POSPAD_Y and  xp < ball.x < xp + taillePad and ball.y < POSPAD_Y + 7.5:
        if -25 < speed.x < 25:
            if speed.x > 0:
                speed.x = 1.1*speed.x
            else:
                speed.x = 1.1*speed.x

            if speed.y > 0:
                speed.y = -1.1*(speed.y)
        else:
            speed.x = 1*speed.x
            speed.y = -1*speed.y
            #the ball is under the paddle -> loose
    elif ball.y > WINDOW_Y:
        speed.x = 3
        speed.y = 3
        ball.y = 420
        ball.x = xp
    
    
while constante.play or constante.helpmenu or constante.menu:

    if constante.helpmenu:
        help_menu()
        
    elif constante.menu:
        menu()
     
    elif constante.play:
        windows.blit(background, (0,0))
        windows.blit(player, (xp,yp))
        for i in liste:
            if i.isDead == False:
                windows.blit(i.pic, (i.posX , i.posY))
                
                
                
##        if brick1.isDead == False:
##            windows.blit(brick1.pic, (brick1.posX,brick1.posY))
##        if brick2.isDead == False:
##            windows.blit(brick2.pic, (brick2.posX,brick2.posY))
##        if brick3.isDead == False:
##            windows.blit(brick3.pic, (brick3.posX,brick3.posY))
##        if brick4.isDead == False:
##            windows.blit(brick4.pic, (brick4.posX,brick4.posY))
##        if brick5.isDead == False:
##            windows.blit(brick5.pic, (brick5.posX,brick5.posY))
##        if brick6.isDead == False:
##            windows.blit(brick6.pic, (brick6.posX,brick6.posY))
##        if brick7.isDead == False:
##            windows.blit(brick7.pic, (brick7.posX,brick7.posY))
##        if brick8.isDead == False:
##            windows.blit(brick8.pic, (brick8.posX,brick8.posY))
##        if brick9.isDead == False:
##            windows.blit(brick9.pic, (brick9.posX,brick9.posY))
##        if brick10.isDead == False:
##            windows.blit(brick10.pic, (brick10.posX,brick10.posY))

        for i in range(4):                      #On regarde 4 fois  pour voir si une autre touche est enfoncée
            for event in pygame.event.get():    #On parcours la liste de tous les événements reçus
                if event.type == QUIT:          #Si un de ces événements est de type QUIT
                    constante.jeu = False       #on quitte le jeu

                if event.type == KEYDOWN:       # si on presse une touche (n'importe laquelle)
                    if event.key == K_RIGHT and xp < 510:
                        xp += 15
                    
                    if event.key == K_LEFT and xp > 10:
                        xp -= 15
        updateBall()
        pygame.display.flip()
