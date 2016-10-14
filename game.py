                     # -*- coding: cp1252 -*-
import pygame
import constante
import menu

import ball
from pygame.locals import *
from time import *
from threading import Timer
pygame.init()

background = pygame.image.load("./Sprites/background/background.jpg")
abscisse_fond = 0
windows.blit(background, (0,0))
font = pygame.font.Font("GearsOfPeace.ttf",36)
player = pygame.image.load("./Sprites/Paddle/paddle.png").convert_alpha()

def place():
    perso = pygame.image.load("paddle.png").convert_alpha()
    posPad = 0

    brick1 = brick()
    brick1.posX = 20
    brick1.posY = 20

    brick2 = brick()
    brick2.posX = 170
    brick2.posY = 20
    
    brick3 = brick()
    brick3.posX = 330
    brick3.posY = 20

    brick4 = brick()
    brick4.posX = 470
    brick4.posY = 20

    brick5 = brick()
    brick5.posX = 620
    brick5.posY = 20

    brick6 = brick()
    brick6.posX = 20
    brick6.posY = 50

    brick7 = brick()
    brick7.posX = 170
    brick7.posY = 50

    brick8 = brick()
    brick8.posX = 330
    brick8.posY = 50

    brick9 = brick()
    brick9.posX = 470
    brick9.posY = 50

    brick10 = brick()
    brick10.posX = 620
    brick10.posY = 50

        
class brick():
	pic = pygame.image.load("brick.png").convert_alpha()
	posX = None
	posY = None
	isDead = False

            
def main():
    while constante.play:
        windows.blit(background, (0,0))
        pygame.key.set_repeat(30,30)
        yp = 0
        xp = 320
        windows.blit(player, (xp,yp))

        for i in range(4):                      #On regarde 4 fois  pour voir si une autre touche est enfoncée
            for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
                if event.type == QUIT:     #Si un de ces événements est de type QUIT
                    constante.jeu = False  #on quitte le jeu

                if event.type == KEYDOWN:           # si on presse une touche (n'importe laquelle)
                    if event.key == K_RIGHT and xp < 600:
                        xp += 2
                    
                    if event.key == K_LEFT and xp > 30:
                        xp -= 2
        place()
        pygame.display.flip()
