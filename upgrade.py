import pygame
from pygame.locals import*
from time import*
from threading import Timer
pygame.init()

class Particle():
    x=None
    y=None
    pic = player = pygame.image.load("Sprites/Particle.png")

def initParti(probability, x ,y):
    if probability == 5:
        particle = Particle()
        particle.x = x
        particle.y = y
        return particle
    
    return false

def updateParticle(window, particle):
    window.blit(particle.pic, (particle.x, particle.y))
    particle.y += 1 
