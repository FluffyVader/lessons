import pygame
from pygame.locals import *
HEIGHT=500
WIDTH=400
FPS=50

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Plane shooter")
planeSprite = pygame.image.load("plane.png")
planeSpriteWidth = planeSprite.get_width()

#planeSpriteHeight = planeSprite.get_height()

running = True
planeX = 0
planeY = 400
plane_velocity=2

while running:
    for event in pygame.event.get():
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_a:
                plane_velocity = -plane_velocity
                pass
            elif event.key == pygame.K_d:
                if planeX<=WIDTH-planeSpriteWidth:
                    plane_velocity = -plane_velocity
                pass
        elif event.type == pygame.QUIT:
            running = False

    
    planeX += plane_velocity


    if planeX <= 0:
        planeX = 0
    elif planeX >= WIDTH-planeSpriteWidth:
        planeX = WIDTH - planeSpriteWidth
    


    screen.fill("black")
    screen.blit(planeSprite,(planeX,planeY))

    clock.tick(FPS)
    pygame.display.flip()