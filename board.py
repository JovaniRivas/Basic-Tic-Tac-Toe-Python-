#import main
import stringFunctions
def print_board(width, height, tic_tac_matrix):
    stringFunctions.print_blank_lines()
    row = height - 1
    col = width - 1
    size = width * height

    for x in range(row + 1):# Number of rows (Must subtract by 1 to get desired rows)
        for y in range(col + 1):#col
            print_string = " " + tic_tac_matrix[x][y] + " "
            print(print_string, end='')
            if (y < col):
                print("|", end='')
        print('')
        if x < row:  # Print horizontal dividers except after the last row
            for z in range(col):  # col
                print("---|", end='')
            print("---")