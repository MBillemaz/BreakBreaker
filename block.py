import pygame
from pygame.locals import*
from time import*
from threading import Timer
pygame.init()

class brick():
    pic = pygame.image.load("./Sprites/Brick/block.png")
    posX = None
    posY = None
    isDead = False
	
def brick_gen():
    liste = []
    posX = 20
    posY = 20
    
    for i in range (0,4):
        testbrick = brick()
        testbrick.posX = posX
        testbrick.posY = posY
        liste.append(testbrick)
        if posX >= 560:
            posX = 20
            posY = posY + 15
        else:
            posX = posX + 45
    return liste

