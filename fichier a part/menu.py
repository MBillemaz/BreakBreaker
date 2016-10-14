            # -*- coding: cp1252 -*-
import pygame
from pygame.locals import *
from time import*
from threading import Timer
import ball
pygame.init()

windows =  pygame.display.set_mode((640, 480))
background = pygame.image.load("background.jpg")
abscisse_fond = 0
windows.blit(background, (0,0))
pygame.key.set_repeat(5,5)
font = pygame.font.Font("GearsOfPeace.ttf",36)
title = font.render("BreakBreaker",1,(255,255,255))
begin = font.render("Begin : Space",1,(255,255,255))
help = font.render("Help : H",1,(255,255,255))
left = pygame.image.load("left.jpg").convert_alpha()
right = pygame.image.load("right.jpg").convert_alpha()
control = font.render("Move right and left", 1, (255,255,255))
action = font.render("Action",1, (255,255,255))
player = pygame.image.load("Sprites/Paddle/paddle.png").convert_alpha()
menu = True
game = False
help_menu = False

xp = 320

#spacebar = pygame.image.load().convert_alpha()
#win = pygame.image.load(
#lose = pygame.image.load(


while menu:
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
                game = True
                menu = False
                ball.initBall()
            if event.key == K_h:
                help_menu = True
                menu = False
            
while help_menu:
    windows.blit(background,(0,0))
    windows.blit(control,(50,200))
    windows.blit(left, (150,200))
    windows.blit(right, (250,200))
    windows.blit(action, (50, 400))
    #windows.blit(
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_space:
                help_menu = False
        
while game:
    

    windows.blit(background,(0,0))
    ball.updateBall(windows, xp)
    for event in pygame.event.get():

        if event.type == K_ESCAPE:
            pygame.quit()
        if event.type == QUIT:  
            pygame.quit()
        if event.type == KEYDOWN:       # si on presse une touche (n'importe laquelle)
                    if event.key == K_RIGHT and xp < 510:
                        xp += 15
                    
                    if event.key == K_LEFT and xp > 10:
                        xp -= 15
    windows.blit(player, (xp,450))  
    pygame.display.flip()    

