import pygame
import random
import math

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

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 20)
textX = 10
textY = 10

#Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('64alien.png'))
    enemyX.append(random.randint(0, 1200))
    enemyY.append(random.randint(50, 250))
    enemyX_change.append(4)
    enemyY_change.append(40)


#.blit means to draw (player-ship on screen)/Type Casting score font...
def show_score(x,y):
    score = font.render("score :"+ str(score_value),True, (255, 255, 255))
    screen.blit(score, (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y,i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    #Subtract px cnt for bullet starting position to center bullet to ship.
    screen.blit(bulletImg, (x - 95, y -130))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX, 2))+ math.pow(enemyY-bulletY, 2))
    if distance < 50:
        return True
    else:
        return False

#Game Loop
#while loop, def running as true. event exists until quit, then terminates.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Keymapping
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
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
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 1148:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]
        # Enemy collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 880
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 1200)
            enemyY[i] = random.randint(50, 250)

        enemy(enemyX[i], enemyY[i], i)
    #Bullet Movement
    if bulletY <= 0:
        bulletY = 880
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()

    pass



