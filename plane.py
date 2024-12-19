import pygame
from pygame.locals import *

# Defines
HEIGHT=500
WIDTH=400
FPS=50

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Plane shooter")
planeSprite = pygame.image.load("plane.png")
planeSpriteWidth = planeSprite.get_width()


running = True
planeX = 0
planeY = 400
default_plane_velocity = 2 # const. Please never modify it in runtime.
current_plane_velocity = 0

#Main Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                current_plane_velocity = -default_plane_velocity
                pass
            elif event.key == pygame.K_d:
                current_plane_velocity = default_plane_velocity
                pass
        elif event.type == pygame.QUIT:
            running = False

    print(f"default_plane_velocity is {default_plane_velocity} current_plane_velocity is {current_plane_velocity}")
    planeX += current_plane_velocity

    # Constain X coordinate
    if planeX <= 0:
        planeX = 0
    elif planeX >= WIDTH - planeSpriteWidth:
        planeX = WIDTH - planeSpriteWidth
    


    screen.fill("black")
    screen.blit(planeSprite,(planeX,planeY))

    clock.tick(FPS)
    pygame.display.flip()