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
enemy_default_plane_velocity = 2
enemy_current_plane_velocity = enemy_default_plane_velocity

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
enemy_plane_sprite_rect = enemy_plane_sprite.get_rect() ###############
enemy_plane_sprite_dead = False

#bullet load
bullet_sprite = pygame.image.load("bullet.png")
bullet_velocity = 20
bullet_srite_rect = bullet_sprite.get_rect()

bulletX = 0
bulletY = planeY - 32
bullet_srite_rect.top = bulletY
bullet_srite_rect.left = planeX + (36 - 16)

is_bullet_spawned = False
#Main Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                current_plane_velocity = -default_plane_velocity
            elif event.key == pygame.K_d:
                current_plane_velocity = default_plane_velocity
            elif event.key == pygame.K_SPACE:
                is_bullet_spawned = True
                bulletX = planeX + (36 - 16)
                bulletY = planeY - 32
                bullet_srite_rect.left = planeX + (36 - 16)
                bullet_srite_rect.top = bulletY

        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                current_plane_velocity = 0


        elif event.type == pygame.QUIT:
            running = False


    # print(f"default_plane_velocity is {default_plane_velocity} current_plane_velocity is {current_plane_velocity}") debug featers
    
    planeX += current_plane_velocity
    enemy_planeX += enemy_current_plane_velocity
    # Constain X coordinate
    if planeX <= 0:
        planeX = 0
    elif planeX >= WIDTH - planeSpriteWidth:
        planeX = WIDTH - planeSpriteWidth

    if enemy_planeX <= 0:
        enemy_planeX = 0
        enemy_current_plane_velocity = -enemy_current_plane_velocity

    elif enemy_planeX >= WIDTH - enemy_plane_Sprite_Width:
        enemy_planeX = WIDTH - enemy_plane_Sprite_Width
        enemy_current_plane_velocity = -enemy_current_plane_velocity

    enemy_plane_sprite_rect.left = enemy_planeX

    screen.fill("black")
    
    screen.blit(planeSprite,(planeX,planeY))
    if not enemy_plane_sprite_dead:
        screen.blit(enemy_plane_sprite,(enemy_planeX,enemy_planeY))
    
    if is_bullet_spawned:
        bulletY -= bullet_velocity
        screen.blit(bullet_sprite,(bulletX, bulletY))
        bullet_srite_rect.top = bulletY


    if pygame.Rect.colliderect(bullet_srite_rect, enemy_plane_sprite_rect) :
        print(f"Collided bullet_srite_rect: {bullet_srite_rect}  enemy_plane_sprite_rect{enemy_plane_sprite_rect}")
        enemy_plane_sprite_dead = True

    #print(enemy_plane_sprite_rect)
    #print(bullet_srite_rect)

    clock.tick(FPS)
    pygame.display.flip()