import pygame


WIDTH = 360
HEIGHT = 480
FPS=30



pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("mygame")
clock = pygame.time.Clock()






running = True
while running:

    clock.tick(FPS)