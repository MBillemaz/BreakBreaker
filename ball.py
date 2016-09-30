import pygame
from pygame.locals import*
from time import*
from threading import Timer

pygame.init()


class Point():
    x=None
    y=None
#Speed of the ball per pixel
speed= Point()
speed.x = 1
speed.y = 1

#constant for dimension of window
WINDOW_X = 640
WINDOW_Y = 480
POSPAD_Y = 400

ball = Point()
 
def initBall():

    window = pygame.display.set_mode((WINDOW_X, WINDOW_Y))

    ballSprite = pygame.image.load("Sprites/ball/ball.png")

    #Get the middle of thwindow
    ball.x = WINDOW_X/2
    ball.y = WINDOW_Y/2

def updateBall():
    #update the position of the ball
    ball.x += speed.x
    ball.y += speed.y

    #update the position of the sprite of the ball
    window.blit(ballSprite,(ballX, ballY))

def collision():
    #Ball and window 
            #If the ball is at the left or right of window -> reverse the speedX
            if ball.x <=0 or ball.x >= WINDOW_X:
                speed.x = -1*speed.x

            #If the ball is at the top of window -> reverse the speedY
            if ball.y <= 0:
                speed.y = -1*speed.y
        
    #Ball and Paddle
            #The Ball is on the paddle
            if ball.y >= POSPAD_Y and  posPad < ball.x < posPad + taillePad:
                speed.x = -1*speed.x
                speed.y = -1*speed.y
            #the ball is under the paddle -> loose
            elif ball.y > POSPAD_Y:
                loose()
    #Ball and Bricks 
