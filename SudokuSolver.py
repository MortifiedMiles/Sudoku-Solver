import math
import pygame

Easy = [[3,7,0,6,0,9,0,2,1],[4,0,0,0,8,0,0,0,3],[0,0,6,3,0,5,7,0,0],
        [6,0,4,0,0,0,3,0,9],[0,9,0,0,3,0,0,8,0],[2,0,7,0,0,0,1,0,4],
        [0,0,1,9,0,8,4,0,0],[5,0,0,0,6,0,0,0,7],[8,2,0,1,0,4,0,9,5]]

Hard = [[0,0,0,8,0,0,0,0,6],[1,7,8,0,2,0,0,0,0],[0,0,0,0,7,0,8,9,0],
          [0,1,0,0,0,2,6,0,0],[7,2,4,0,6,8,0,1,3],[3,0,0,0,0,0,2,0,4],
          [0,0,0,0,0,5,0,7,9],[0,9,0,7,3,0,1,0,0],[0,6,0,0,0,0,0,0,0]]

Extreme = [[0,4,0,6,0,1,0,5,0],[0,0,2,0,0,0,0,1,0],[0,0,3,0,0,8,0,6,0],
            [5,0,0,0,0,7,0,8,0],[0,0,4,0,0,6,0,0,3],[0,0,0,0,0,0,0,0,0],
            [0,0,7,0,0,4,0,0,9],[0,0,0,2,1,0,0,0,0],[0,2,0,0,7,0,0,0,8]]

# blanks stores the location of cells which have been altered [row,column,row,column,...]
blanks = []
def brutishSudokuSolver(matrix, row, column):
    # if the cell is the last remaining in the matrix, pass
    if row == len(matrix) and column == len(matrix):
        pass
    # elif there are any broken rules on a selected cell, increment that cell
    elif len(blanks) >= 2 and checker(matrix, (blanks[-2]), (blanks[-1])):
        matrix[blanks[-2]][blanks[-1]] += 1
        # if the selected cell is now bigger than 9, delete the entry from blanks, and increment the previously chosen cell
        if matrix[blanks[-2]][blanks[-1]] > 9:
            matrix[blanks[-2]][blanks[-1]] = 0
            del blanks[-2:]
            while matrix[blanks[-2]][blanks[-1]] == 9:
                matrix[blanks[-2]][blanks[-1]] = 0
                del blanks[-2:]
            matrix[blanks[-2]][blanks[-1]] += 1
            row, column = blanks[-2], blanks[-1]
    # otherwise find the next empty cell
    else:
        # iterate through each row, 
        blank = False
        while row < len(matrix) and blank == False:
            if column == len(matrix):
                column = 0
            while column < len(matrix) and blank == False:
                if (matrix[row][column]) == 0:
                        blanks.append(row)
                        blanks.append(column)
                        matrix[row][column] += 1
                        blank = True
                column += 1
            row += 1
        blank = False


def checker(matrix, row = 0, column = 0):
    # checks columns, rows, and sections for a match to matrix[row][column]
    # if there is a match, the function returns false, if not, the function returns true
    check = False
    while check == False:
        for num in range(0,9):
            #check if there is a match in the column
            if matrix[num][column] == matrix[row][column] and num != row:
                check = True
            #check if there is a match in the row
            elif matrix[row][num] == matrix[row][column]and num != column:
                check = True
        #check if there is a match in the section
        for r in range(0,3):
            for c in range(0,3):
                if matrix[row][column] == matrix[math.floor(row/3)*3+r][math.floor(column/3)*3+c] and [row,column] != [math.floor(row/3)*3+r, math.floor(column/3)*3+c]:
                    check = True
        return check

def drawNums(matrix, window, black, gridWH, origin):
    cell_border = 60
    celldimX = celldimY = (gridWH/len(matrix)) - (cell_border * 2)
    for row in range(0, len(matrix)):
        for column in range(0, len(matrix)):
            if matrix[row][column] > 0:
                num = str(matrix[row][column])
                font = pygame.font.SysFont('Comic Sans', cell_border)
                text_surface = font.render(num, True, black)
                pos = (origin[0] + (celldimY * column) + (2*column*cell_border) + 1/2 + cell_border/3, 
                       origin[1] + (celldimX * row) + (2*row*cell_border) + 1/2)
                window.blit(text_surface, pos)



def draw_square_grid(origin, gridWH, cells, window, black):
    CONTAINER_WIDTH_HEIGHT = gridWH
    cont_x, cont_y = origin

    # Draw grid border
    # Top left to right
    pygame.draw.line(window, black, (cont_x, cont_y), (CONTAINER_WIDTH_HEIGHT + cont_x, cont_y))
    # Bottom left to right
    pygame.draw.line(window, black, (cont_x, cont_y + CONTAINER_WIDTH_HEIGHT), (CONTAINER_WIDTH_HEIGHT + cont_x, cont_y + CONTAINER_WIDTH_HEIGHT))
    # Left top to bottom
    pygame.draw.line(window, black, (cont_x, cont_y), (cont_x, cont_y + CONTAINER_WIDTH_HEIGHT))
    # Right top to bottom
    pygame.draw.line(window, black, (cont_x + CONTAINER_WIDTH_HEIGHT, cont_y), (CONTAINER_WIDTH_HEIGHT + cont_x, cont_y + CONTAINER_WIDTH_HEIGHT))

    # Get cell size
    cell_size = CONTAINER_WIDTH_HEIGHT/cells

    # Vertical Divisions
    for x in range(cells):
        pygame.draw.line(window, black, (cont_x + (cell_size * x), cont_y), (cont_x + (cell_size * x), CONTAINER_WIDTH_HEIGHT + cont_y))
    #   # Horizontal Divisions
        pygame.draw.line(window, black, (cont_x, cont_y + (cell_size * x)), (cont_x + CONTAINER_WIDTH_HEIGHT, cont_y + (cell_size * x)))

