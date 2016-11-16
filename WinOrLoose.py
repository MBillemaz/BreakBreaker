import pygame
from pygame.locals import *
from time import*
from threading import Timer
import menu
def win(windows):
	pic = pygame.image.load("Sprites/win.png")
	windows.blit(pic, (0,0))
	pygame.display.flip()
	for event in pygame.event.get():
                if event.type == K_ESCAPE:
                        menu.win = False
                        menu.menu = True
