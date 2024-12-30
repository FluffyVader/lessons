import pygame
from pygame.locals import *

# Defines
HEIGHT=500
WIDTH=400
FPS=50

#courdinates, velocity and name
running = True
planeX = 0
planeY = 400
default_plane_velocity = 2  # const Please never modify it in runtime.
current_plane_velocity = 0

enemy_planeX = 0
enemy_planeY = 0


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Plane shooter")

#my plane loading
planeSprite = pygame.image.load("plane.png")
planeSpriteWidth = planeSprite.get_width()

#enemy loading
enemy_plane_sprite = pygame.image.load("plane.png")
enemy_plane_Sprite_Width = enemy_plane_sprite.get_width()
enemy_plane_sprite = pygame.transform.rotate(enemy_plane_sprite, 180)

#Main Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                current_plane_velocity = -default_plane_velocity
            elif event.key == pygame.K_d:
                current_plane_velocity = default_plane_velocity
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                current_plane_velocity = 0
       
        elif event.type == pygame.QUIT:
            running = False

    # print(f"default_plane_velocity is {default_plane_velocity} current_plane_velocity is {current_plane_velocity}") debug featers
    
    planeX += current_plane_velocity

    # Constain X coordinate
    if planeX <= 0:
        planeX = 0
    elif planeX >= WIDTH - planeSpriteWidth:
        planeX = WIDTH - planeSpriteWidth


    screen.fill("black")
    
    screen.blit(planeSprite,(planeX,planeY))
    screen.blit(enemy_plane_sprite,(enemy_planeX,enemy_planeY))
    
    clock.tick(FPS)
    pygame.display.flip()