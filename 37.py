import pygame
maze = [
    [1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1],
    [1,1,0,1,1,0,1],
    [1,0,0,0,1,1,1],
    [1,0,1,0,0,0,1],
    [1,1,1,0,1,0,1],
    [1,0,0,0,1,0,0],
    [1,1,1,1,1,1,1]
]
character_position = [1,1]
cell_side_size= 30
width = cell_side_size * len(maze)
height = cell_side_size * len(maze[0])
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("maze")
running = True
def draw_maze():
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            color = (0,0,0)
            if maze[row][col] == 1:
                color = (255, 255, 255)
            #else:
            #    color = (0, 0, 0)
            pygame.draw.rect(window, color, (col*cell_side_size, row*cell_side_size, cell_side_size, cell_side_size))

def draw_player():
    pygame.draw.rect(window, (255, 255,0), (character_position[0]*cell_side_size, character_position[1]*cell_side_size, cell_side_size, cell_side_size))

def change_character_pos(dx, dy):
    new_x = character_position[0]+dx
    new_y = character_position[1]+dy
    if maze[new_x][new_y] == 0:
        character_position[0] = new_x
        character_position[1] = new_y
        if new_x == len(maze[0])-1:
            running = False
            font = pygame.font.SysFont("couriernew",10,50)
            text = font.render("You have finished the maze!", False, "Yellow")
            window.blit(text, (0,0))
