from functions import *
from config import *
import pygame


# Settings
pygame.init()
screen = pygame.display.set_mode((screen_size,screen_size+100))

# Starting variavles
tmp_pressed = False
tmp_keyboard = [False, False, False]
cells = generate_table(n)
solution = [[False for _ in range(n)] for _ in range(n)]

# Game flow
while True:

    draw(screen, screen_size, n, cells, solution, show_solution)

    # Input and interaction
    pygame.event.get()
    mouse_pressed = pygame.mouse.get_pressed()[0]
    keys = pygame.key.get_pressed()

    if mouse_pressed:
        tmp_pressed = True

    if not mouse_pressed and tmp_pressed:
        mouse_pos = pygame.mouse.get_pos()
        square = find_cell(mouse_pos, screen_size/n)
        cells = invert_cells(square, n, cells)
        solution[square[0]][square[1]] = False
        tmp_pressed = False

    if keys[pygame.K_ESCAPE]: break

    if keys[pygame.K_s]: tmp_keyboard[0] = True

    if not keys[pygame.K_s] and tmp_keyboard[0]:
        show_solution = not show_solution
        tmp_keyboard[0] = False

    if keys[pygame.K_n]: tmp_keyboard[1] = True

    if not keys[pygame.K_n] and tmp_keyboard[1]:
        cells = generate_table(n)
        tmp_keyboard[1] = False

    if keys[pygame.K_c]: tmp_keyboard[2] = True

    if not keys[pygame.K_c] and tmp_keyboard[2]:
        solution = best_solution(cells, n)
        tmp_keyboard[2] = False
