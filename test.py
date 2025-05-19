import numpy as np

Easy = [[3,7,0,6,0,9,0,2,1],[4,0,0,0,8,0,0,0,3],[0,0,6,3,0,5,7,0,0],
        [6,0,4,0,0,0,3,0,9],[0,9,0,0,3,0,0,8,0],[2,0,7,0,0,0,1,0,4],
        [0,0,1,9,0,8,4,0,0],[5,0,0,0,6,0,0,0,7],[8,2,0,1,0,4,0,9,5]]


'''def brutishSudokuSolver(matrix, row = 0, column = 0):
    if row == len(matrix) and column == len(matrix):
        pass
    #iterates through each row
    while row < len(matrix):
        if column == len(matrix):
            column = 0
        #iterates through each cell in that row
        while column < len(matrix):
            if len(blanks) >= 2 and row == blanks[-2] and column == blanks[-1]:
                matrix[row][column] += 1
                while checker(matrix, row, column):
                    #check the grid for any broken rules, and if there are increment and recheck
                    matrix[row][column] += 1
                    
            if matrix[row][column] == 0:
                #if the cell is blank, or the same as the last cell stored, add 1
                matrix[row][column] += 1

                while checker(matrix, row, column):
                    #check the grid for any broken rules, and if there are increment and recheck
                    matrix[row][column] += 1
                #add the adjusted cell to the list of blanks
                blanks.append(row)
                blanks.append(column)
            


            if matrix[row][column] > 9:
                #if the cell exceeds the maximum, reset it, delete it from blanks, increment the previously edited cell, rerun the iterator from that cell
                matrix[row][column] = 0
                del blanks[-2:]
                if len(blanks) >= 2:
                    brutishSudokuSolver(matrix, blanks[-2], blanks[-1])
                brutishSudokuSolver(matrix)
                    
            column += 1
        row += 1
    print(matrix)'''