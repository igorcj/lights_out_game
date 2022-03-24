import pygame

# Square size
n = 5

# Screen resolution
screen_size = 800

# Proportion of the resolution dots on the squares [0,1]
solutions_dots_proportion = 0.12

# Start showing solution (Bool)
show_solution = False

# On squares background color
on_cell_background = (255,255,255)

# Off squares background color
off_cell_background = (0,0,0)

# Outer squares grid color
grid_color = (100,100,100)

# Inside squares solution circles color
solution_circle_color = (0,0,200)

# Header text backgound color
text_background = (0, 0, 0)

# Header text color
text_color = (255, 255, 255)

# Header text fonts
pygame.font.init()
title_font = pygame.font.Font('freesansbold.ttf', 32)
font = pygame.font.Font('freesansbold.ttf', 20)
