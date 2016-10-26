import pygame
from pygame.locals import *
from time import*
from threading import Timer

def win(windows):
	pic = pygame.image.load("Sprites/win.png")
	windows.blit(pic, (0,0))
	pygame.display.flip()
	for event in pygame.event.get():
                if event.type == K_ESCAPE:
                        win = False
                        menu = True
		

def loose(windows):
        pic = pygame.image.load("Sprites/loose.png")
	windows.blit(pic, (0,0))
	pygame.display.flip()
	for event in pygame.event.get():
                if event.type == K_ESCAPE:
                        loose = False
                        menu = True
