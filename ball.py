import pygame
import WinOrLoose
from pygame.locals import*
from time import*
from threading import Timer
pygame.init()


class Point():
    x=None
    y=None
#Speed of the ball per pixel
speed= Point()
speed.x = 4
speed.y = 4
TaillePad = 125
#constant for dimension of window
WINDOW_X = 640
WINDOW_Y = 480
POSPAD_Y = 450
BALL_HEIGHT = 16

vie = 3

ball = Point()
ballSprite = pygame.image.load("Sprites/ball/ball.png")
def initBall():

    #Get the middle of thwindow
    ball.x = WINDOW_X/2+ 15
    ball.y = 430

def updateBall(windows, xp):
    #update the position of the ball
    ball.x += speed.x
    ball.y += speed.y

    #update the position of the sprite of the ball
    windows.blit(ballSprite,(ball.x, ball.y))
    collision(xp, windows)

def collision(xp, windows):
    #Ball and window 
    #If the ball is at the left or right of window -> reverse the speedX
    global vie
    if ball.x <=0 or ball.x >= WINDOW_X - 16:
        speed.x = -1*speed.x

    #If the ball is at the top of window -> reverse the speedY
    if ball.y <= 0:
        speed.y = -1*speed.y
        
    #Ball and Paddle
            #The Ball is on the paddle
    if ball.y + BALL_HEIGHT >= POSPAD_Y and  xp < ball.x + BALL_HEIGHT < xp + TaillePad and ball.y < POSPAD_Y + 7.5:
        if -25 < speed.x < 25:
            speed.x = 1.1*speed.x

            if speed.y > 0:
                speed.y = -1.1*(speed.y)
        else:
            speed.x = 1*speed.x
            speed.y = -1*speed.y
            #the ball is under the paddle -> loose
    elif ball.y > WINDOW_Y:
        vie = vie-1
        speed.x = 5
        speed.y = 5
        ball.x = WINDOW_X/2
        ball.y = WINDOW_Y/2
                                                

def block_coll(liste):
    for i in liste:
        if i.isDead == False:
            if i.posX <= ball.x <= i.posX + 46:
                if i.posY + 19 >= ball.y >= i.posY + 15:
                    i.isDead = True
                    speed.y = -1*speed.y
                elif i.posY +2 >= ball.y >= i.posY:
                    i.isDead = True
                    speed.y = -1*speed.y
                    print("lol")
                if i.posY <= ball.y <= i.posY + 14:
                    i.isDead = True
                    speed.x = -1*speed.x
def perdreVie():
    vie = vie-1

def getVie():
    return vie

def setVie(newVie):
    vie = newVie
