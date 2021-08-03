import pygame
import random

#initialize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((1250,1000))

#background
background = pygame.image.load('backgroundsi.png')

#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spcalieno.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('oship.png')
playerX = 575
playerY = 880
playerX_change = 0

#Bullet "ready"- you can't see bullet... "fire"- bullet is moving.
bulletImg = pygame.image.load('starblast.png')
bulletX = 0
bulletY = 880
bulletX_change = 0
bulletY_change = 15
bullet_state = "ready"

#Enemy
enemyImg = pygame.image.load('64alien.png')
enemyX = random.randint(0, 1200)
enemyY = 200
enemyX_change = 4
enemyY_change = 40


#.blit means to draw (player-ship on screen)
def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    #Subtract px cnt for bullet starting position to center bullet to ship.
    screen.blit(bulletImg, (x - 95, y -130))

#Game Loop
#while loop, def running as true. event exists until quit, then terminates.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    #RGB/always put screen first, so the screen is drawn first , then the images are drawn next.
    screen.fill((250,0,0))
    #Background IMG
    screen.blit(background, (0,0))


    playerX += playerX_change
    #Created boundaries .. 0 is 0; (1200 - (icon x48px) = 1152)
    if playerX <= 0:
        playerX = 0
    elif playerX >=1186:
        playerX = 1186

    #Enemy boundaries/Movement (difference in x px - .png px)
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >=1148:
        enemyX_change = -4
        enemyY += enemyY_change

    if bullet_state is "fire":
        fire_bullet (playerX, bulletY)
        bulletY -= bulletY_change

    enemy(enemyX, enemyY)
    player(playerX, playerY)

    pygame.display.update()

    pass



