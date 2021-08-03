import pygame

#initialize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((1200,1000))

#Key Bind


#Game Loop
#while loop, def running as true. event exists until quit, then terminates.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pass



