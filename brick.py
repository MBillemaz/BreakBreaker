import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((640, 480))
fenetre.blit("bg.png", (0,0))

class brick():
	pic = pygame.image.load("brick.png").convert_alpha()
	posX = None
	posY = None
	isDead = False

perso = pygame.image.load("paddle.png").convert_alpha()
posPad = 0

brick1 = brick()
brick1.posX = 20
brick1.posY = 20

brick2 = brick
brick2.posX = 170
brick2.posY = 20

brick3 = brick
brick3.posX = 330
brick3.posY = 20

brick4 = brick
brick4.posX = 470
brick4.posY = 20

brick5 = brick
brick5.posX = 620
brick5.posY = 20

brick6 = brick
brick6.posX = 20
brick6.posY = 50

brick7 = brick
brick7.posX = 170
brick7.posY = 50

brick8 = brick
brick8.posX = 330
brick8.posY = 50

brick9 = brick
brick9.posX = 470
brick9.posY = 50

brick10 = brick
brick10.posX = 620
brick10.posY = 50

game = False
menu = True
commande = False

while game:
	
	
	
    for event in pygame.event.get():

        if event.type == K_ESCAPE:
		
            game = False
			menu = True
		
		if envent.type == QUIT:
			
			game = False
			
		if event.type == KEYDOWN:
			
			if event.type == K_RIGHT and posPad < 637:
				posPad = posPad + 3
				
			if event.type == K_LEFT and posPad > 3:
				posPad = posPad - 3
		
		fenetre.blit(perso, (posPad,400))
		if brick1.isdead == False:
			fenetre.blit(brick1.pic, (brick1.posX,brick1.posY))
		if brick1.isdead == False:
			fenetre.blit(brick2.pic, (brick2.posX,brick2.posY)
		if brick1.isdead == False:
			fenetre.blit(brick3.pic, (brick3.posX,brick3.posY))
		if brick1.isdead == False:
		fenetre.blit(brick4.pic, (brick4.posX,brick4.posY))
		if brick1.isdead == False:
		fenetre.blit(brick5.pic, (brick5.posX,brick5.posY))
		if brick1.isdead == False:
		fenetre.blit(brick6.pic, (brick6.posX,brick6.posY))
		if brick1.isdead == False:
		fenetre.blit(brick7.pic, (brick7.posX,brick7.posY))
		if brick1.isdead == False:
		fenetre.blit(brick8.pic, (brick8.posX,brick8.posY))
		if brick1.isdead == False:
		fenetre.blit(brick9.pic, (brick9.posX,brick9.posY))
		if brick1.isdead == False:
		fenetre.blit(brick10.pic, (brick10.posX,brick10.posY))
		
		pygame.display.flip()
			
 
pygame.quit()