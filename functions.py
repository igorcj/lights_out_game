from config import *
import numpy as np
import pygame
from pulp import *


# Generate random game with size n
def generate_table(n):
    cells = [[False for _ in range(n)] for _ in range(n)]
    for i in range(int(n*n/2)):
        i = np.random.randint(0,n)
        j = np.random.randint(0,n)
        cells = invert_cells((i,j), n, cells)
    return cells


# Find cell of table based ond mouse position
def find_cell(mouse_position, square_size):
    return (int(np.floor(mouse_position[0]/square_size)),
            int(np.floor((mouse_position[1]-100)/square_size)))


# Invert cells corresponding to a click on certain square
def invert_cells(square, n, cells):
    i, j = square
    cells_list = [t for t in [(i,j),(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
                  if t[0]>=0 and t[1]>=0 and t[0]<=n-1 and t[1]<=n-1]
    for i,j in cells_list:
        cells[i][j] = not cells[i][j]
    return cells


# Draw table with all features
def draw(screen, screen_size, n, cells, solution, show_solution):
    square_size = screen_size/n
    pygame.draw.rect(screen, off_cell_background, pygame.Rect(0, 0, screen_size, screen_size+100))

    title = title_font.render('Lights Out Game', True, text_color, text_background)
    titleRect = title.get_rect()
    titleRect.center = (screen_size//2, 25)
    screen.blit(title, titleRect)
    
    text = font.render('ESC = sair        S = exibir solução        C = calcular        N = novo jogo', True, text_color, text_background)
    textRect = text.get_rect()
    textRect.center = (screen_size//2, 75)
    screen.blit(text, textRect)

    for i in range(n):
        for j in range(n):
            pygame.draw.rect(screen, on_cell_background, pygame.Rect(i*square_size, j*square_size+100, square_size, square_size), not cells[i][j])
            pygame.draw.rect(screen, grid_color, pygame.Rect(i*square_size, j*square_size+100, square_size, square_size), 1)
            if show_solution and solution[i][j]:
                pygame.draw.circle(screen, solution_circle_color, ((i+0.5)*square_size, (j+0.5)*square_size+100), 0.5*solutions_dots_proportion*square_size)
    pygame.display.flip()


# Find best solution with MIP
def best_solution(cells, n):
    prob = LpProblem("game", LpMinimize)
    X = [[LpVariable(f"X{i}{j}", cat='Binary') for i in range(n)] for j in range(n)]
    T = [[LpVariable(f"T{i}{j}", cat='Integer') for i in range(n)] for j in range(n)]
    prob += sum([sum(k) for k in X]), "Z"

    for i in range(n):
        for j in range(n):
            s = [X[i][j]]
            if i>0: s.append(X[i-1][j])
            if i<n-1: s.append(X[i+1][j])
            if j>0: s.append(X[i][j-1])
            if j<n-1: s.append(X[i][j+1])
            prob += sum(s) - cells[i][j] == 2 * T[i][j]

    prob.solve()

    res = [v.varValue for v in prob.variables()][n*n:]
    return [res[i:n*n:n] for i in range(n)]
