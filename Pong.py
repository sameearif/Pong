import pygame
import random
import math
from pygame import mixer

pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()

#Make Screen
screen = pygame.display.set_mode((800, 600))

# Background Fucntion
backgroundImg = pygame.image.load('BG.png')
midImg = pygame.image.load('MidLine.png')
midImg = pygame.transform.scale(midImg, (10, 600))
goalImg = pygame.image.load('Goal.png')
goalImg = pygame.transform.scale(goalImg, (10, 600))
wallImg = pygame.image.load('Wall.png')
def drawBackground():
    screen.blit(backgroundImg, (0, 0))
    screen.blit(midImg, (395, 0))
    screen.blit(goalImg, (0, 0))
    screen.blit(goalImg, (790, 0))
    screen.blit(wallImg, (0, 0))
    screen.blit(wallImg, (0, 588))

#Player Function
playerOneSpeed = 0
playerTwoSpeed = 0
playerOneImg = pygame.image.load('Player.png')
playerOneImg = pygame.transform.scale(playerOneImg, (20, 100))
playerOneX = 100
playerOneY = 242
playerTwoImg = pygame.image.load('Player.png')
playerTwoImg = pygame.transform.scale(playerTwoImg, (20, 100))
playerTwoX = 660
playerTwoY = 242
def drawPlayerOne(x, y):
    screen.blit(playerOneImg, (x, y))
def drawPlayerTwo(x, y):
    screen.blit(playerTwoImg, (x, y))

#Ball Function
ballImg = pygame.image.load('Ball.png')
ballImg = pygame.transform.scale(ballImg, (30, 30))
ballX = 385
ballY = 285
ballSpeedX = random.uniform(-4, 4)
ballSpeedY = random.uniform(-4, 4)
while ballSpeedX >= -2 and ballSpeedX <= 2:
    ballSpeedX = random.randint(-4, 4)
while ballSpeedY >= -2 and ballSpeedY <= 2:
    ballSpeedY = random.randint(-4, 4)
def drawBall(x, y):
    screen.blit(ballImg, (x, y))

#Collision Function
def collision():
    if((ballY >= playerOneY and ballY <= playerOneY + 100) and 
        (ballX >= playerOneX and ballX <= playerOneX + 5)):
           return True
    if((ballY >= playerTwoY and ballY <= playerTwoY + 100) and 
       (ballX >= playerTwoX - 20 and ballX <= playerTwoX)):
           return True

#Wall collision
def wallCollision():
    if(ballY >= 570 or ballY <= 0):
        return True

#CountDown
timer_font = pygame.font.Font("FFFFORWA.TTF", 50)
timer_sec = 3
timer_text = timer_font.render("03", True, (135, 206, 250))
timer = pygame.USEREVENT + 1                                                
pygame.time.set_timer(timer, 1000)

gameOver = False
running = True
begin = False
while running:
    screen.fill((0, 0, 0))
    drawBackground()
    drawPlayerOne(playerOneX, playerOneY)
    drawPlayerTwo(playerTwoX, playerTwoY)
    drawBall(ballX, ballY)
    for event in pygame.event.get():
        if event.type == timer:
            if timer_sec > 1:
                timer_sec -= 1
                timer_text = timer_font.render("%02d" % timer_sec, True, (135, 206, 250))
            else:
                pygame.time.set_timer(timer, 0)
                begin = True
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerTwoSpeed = -5
            if event.key == pygame.K_DOWN:
                playerTwoSpeed = 5
            if event.key == pygame.K_w:
                playerOneSpeed = -5
            if event.key == pygame.K_s:
                playerOneSpeed = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerTwoSpeed = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerOneSpeed = 0
    if begin == True:
        ballX += ballSpeedX
        ballY += ballSpeedY
    playerOneY += playerOneSpeed
    playerTwoY += playerTwoSpeed
    if collision():
        if ballSpeedX < 0:
            ballSpeedX -= 1
        else:
            ballSpeedY += 1
        if ballSpeedY < 0:
            ballSpeedY -= 1
        else:
            ballSpeedY += 1
        ballSpeedX *= -1
        if random.randint(0, 1) == 0:
            ballSpeedY *= -1
    if wallCollision():
        ballSpeedY *= -1
    if begin == False:
        screen.blit(timer_text, (370, 20))
    pygame.display.update()
    fpsClock.tick(FPS)
