            # -*- coding: cp1252 -*-
import pygame
from pygame.locals import *
from time import*
from threading import Timer
import ball
import block
pygame.init()

WINDOW_X = 640
WINDOW_Y = 480
windows =  pygame.display.set_mode((WINDOW_X, WINDOW_Y))

abscisse_fond = 0
pygame.key.set_repeat(5,5)

font = pygame.font.Font("GearsOfPeace.ttf",36)
title = font.render("BreakBreaker",1,(255,255,255))
begin = font.render("Begin : Space",1,(255,255,255))
help = font.render("Help : H",1,(255,255,255))
control = font.render("Move right and left", 1, (255,255,255))
action = font.render("Action",1, (255,255,255))

background = pygame.image.load("Sprites/background/background.jpg")
left = pygame.image.load("Sprites/menu/left.jpg").convert_alpha()
right = pygame.image.load("Sprites/menu/right.jpg").convert_alpha()
player = pygame.image.load("Sprites/Paddle/paddle.png").convert_alpha()

windows.blit(background, (0,0))
win = False

menu = True
game = False
help_menu = False

xp = WINDOW_X/2
liste = []

vie = 3

win = pygame.image.load("Sprites/win.png")
loose = pygame.image.load("Sprites/loose.png")

while menu == True or game == True or ball.getVie() == 0:
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
                    win = False
                    ball.initBall()
                    liste = block.brick_gen()
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
    #Tant que l'on a toujours des vies        
    while game and ball.getVie() > 0 and win == False:
        
        windows.blit(background,(0,0))
        ball.updateBall(windows, xp)
        for event in pygame.event.get():
            if event.type == QUIT:  
                pygame.quit()
            if event.type == KEYDOWN:       # si on presse une touche (n'importe laquelle)
                        if event.type == K_ESCAPE:
                            pygame.quit()
                        if event.key == K_RIGHT and xp < 510:
                            xp += 15
                        
                        if event.key == K_LEFT and xp > 10:
                            xp -= 15
        windows.blit(player, (xp,450))
        ball.block_coll(liste)
        for i in liste:
                if i.isDead == False:
                    windows.blit(i.pic, (i.posX , i.posY))
        pygame.display.flip()
        win = True
        for i in liste:
            if i.isDead == False:
                win = False
    #Si on a plus de vie
    while ball.getVie() == 0:
        windows.blit(loose, (0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:  
                pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                ball.setVie(3)
                menu = True
                game = False
                print(ball.getVie())
    while win == True:
        pic = pygame.image.load("Sprites/win.png")
        windows.blit(pic,(0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:  
                pygame.quit()
            if event.key == K_ESCAPE:
                ball.setVie(3)
                win = False
                menu = True
                game = False
