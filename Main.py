import pygame
import sys
from pygame.locals import *
from SudokuSolver import *

# Define constants
black = (0,0,0)
grey = (160, 160, 160)
screen_width = 800
screen_height = 800
frames_per_second = 10000

# Initialize World
pygame.init()
window = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Initialize Variables
initialRow = 0
initialColumn = 0
blanks = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:           
                pygame.quit()  
                sys.exit()

        if event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()
    

    window.fill(grey)
    draw_square_grid((50,50), 700, len(Easy), window, black)
    drawNums(Extreme, window, black, 700, (50,50))
    brutishSudokuSolver(Extreme, initialRow, initialColumn)


    pygame.display.update()
    clock.tick(frames_per_second)