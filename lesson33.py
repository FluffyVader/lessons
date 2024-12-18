import pygame
from pygame.locals import *

WIDTH = 360
HEIGHT = 480
FPS=30


pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
#bgColorWhite = [255,255,255]
bgColorPurple = (128,0,128)
#screen.fill("blue")
#screen.fill(bgColorWhite)

screen.fill(bgColorPurple)
pygame.display.set_caption("mygame")
clock = pygame.time.Clock()

r = pygame.Rect(0, 0, 200, 80)
pygame.draw.rect(screen, (255, 255, 0), r)
pygame.draw.ellipse(screen, (255, 100, 0), r)
pygame.draw.line(screen, (0, 0, 0), (100, 100), (50, 300), 20)
running = True
while running:
	# for loop through the event queue
    for event in pygame.event.get():
        
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            
            # If the Backspace key has been pressed set
            # running to false to exit the main loop
            if event.key == K_BACKSPACE:
                running = False
                
        # Check for QUIT event
        elif event.type == QUIT:
            running = False

    clock.tick(FPS)
    # Update the display using flip
    pygame.display.flip()