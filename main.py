#Simple Tic Tac Toe Game
import board
import stringFunctions

#########
#if __name__ == '__main__':

def main():
    # Print the main menu and get the option wanted by the user
    stringFunctions.print_dash()
    print('Tic-Tac-Toe')
    print('Main Menu')
    stringFunctions.print_dash()
    print('1. Player vs CPU')
    print('2. Player vs Player')
    print('3. CPU vs CPU')
    print("\nSelect a game mode!")
    stringFunctions.print_dash()
    option = get_valid_integers(1, 3)

    # Selected options trigger certain flags
    match option:
        case 1:
            print("Player vs CPU")
            CPU_flag = 1
            CPU2_flag = 0
        case 2:
            print("Player vs Player")
            CPU_flag = 0
            CPU2_flag = 0
        case 3:
            print("CPU vs CPU")
            CPU_flag = 1
            CPU2_flag = 1

    # If CPU is playing, determine difficulty level
    if CPU_flag:
        print_difficulty_options()
        CPU_difficulty = get_valid_integers(1, 3)
        match CPU_difficulty:
            case 1:
                print("Easy")
            case 2:
                print("Medium")
            case 3:
                print("Hard")
    if CPU2_flag:
        print_difficulty_options()
        print("(CPU #2)")
        CPU_difficulty2 = get_valid_integers(1, 3)
        match CPU_difficulty2:
            case 1:
                print("Easy")
            case 2:
                print("Medium")
            case 3:
                print("Hard")

    # Board Size
    print_board_options()
    board_option = get_valid_integers(1, 3)
    match board_option:
        case 1:
            boardWidth = 3
            boardHeight = 3
        case 2:
            boardWidth = 4
            boardHeight = 4
        case 3:
            boardWidth = 5
            boardHeight = 5

    #initialize the board and start the game
    tic_tac_matrix = matrixInitialization(boardWidth, boardHeight)
    tic_tac_toe_game(CPU_flag, CPU2_flag, tic_tac_matrix)



def print_difficulty_options():
    stringFunctions.print_dash()
    print('Select a difficulty level for the CPU')
    print('1. Easy')
    print('2. Medium')
    print('3. Hard')
    stringFunctions.print_dash()

def print_board_options():
    stringFunctions.print_dash()
    print('Select a board size')
    print('1. 3x3')
    print('2. 4x4')
    print('3. 5x5')
    stringFunctions.print_dash()

def matrixInitialization(width, height):
    return [[' '] * width for x in range(height)]

def get_valid_integers(x, y): # range from x to y
    # Getting input from the user to select CPU difficulty
    while True:
        try:
            valid_int = int(input("Input: "))

            if x <= valid_int <= y:
                return valid_int
            else:
                print(f"Please enter a valid number between {x} and {y}.")
        except ValueError:
            print(f"Please enter a valid number between {x} and {y}.")

def tic_tac_toe_game(player1, player2, initial_board):
    #Going to set this up
    player1 = 'X'
    player2 = 'O'
    print("Game On!!!")
    width = len(initial_board)
    height = len(initial_board)


    board.print_board(width, height, initial_board)
    print(f"Player 1 is {player1}")
    print(f"Player 2 is {player2}")
    while True:
        stringFunctions.print_dash()

        print(f"Player one ({player1}) turn. ")
        print("Please enter a coordinate (column number, row number)")
        print("Note: (1,1) is top left corner")
        while True:
            print("Column Number")
            col = get_valid_integers(1, len(initial_board))
            print("Row Number",)
            row = get_valid_integers(1, len(initial_board))
            if (initial_board[row - 1][col - 1] == ' '):
                initial_board[row - 1][col - 1] = player1
                break
            else:
                print("There is already a value at this position, please try again.")
        board.print_board(width, height, initial_board)
        print("Check to see if player 1 has won")
        if (check_for_win(player1, initial_board)):
            print("PLAYER 1 HAS WON")
            main()
'''
        print(f"Player two ({player2}) turn. ")
        while True:
            print("Column Number")
            col = get_valid_integers(1, len(initial_board))
            print("Row Number", )
            row = get_valid_integers(1, len(initial_board))
            if (initial_board[row - 1][col - 1] == ' '):
                initial_board[row - 1][col - 1] = player2
                break
            else:
                print("There is already a value at this position, please try again.")
        board.print_board(width, height, initial_board)
        print("Check to see if player 2 has won")
        if (check_for_win(player2, initial_board)):
            print("PLAYER 2 HAS WON")
            main()'''

def check_for_win(player, current_board):
    row = len(current_board)
    col = len(current_board)

    # iterate through each row and check to see if any rows have a full match
    for i in range(row):
        if all(cell == player for cell in current_board[i]):
            return True

    # iterate through each column and check to see if there is a full match
    for j in range(col):
        if all(current_board[i][j] == player for i in range(row)):
            return True

    # iterate through the diagonal spaces
    # 0,0   1,1     2,2 (This checks top left -> bottom right diagonal)
    if all(current_board[m][m] == player for m in range(row)):
        return True
    # need to check for diagonal (bottom left -> top right
    # (0,2) (1, 1) (2,0)
    if all(current_board[row - 1 - m][m] == player for m in range(row)):
        return True

    return False


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
main()
