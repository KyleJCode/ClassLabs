'''
Name: Kyle Jeter
Due Date: 11/10/2023
Description: Program is to run Tic-Tac-Toe games until user tells the program to stop
'''

def print_board(board):
    print(("-" * 17) + "\n|R/C| 0 | 1 | 2 |")
    print(("-" * 17) + "\n| 0 |", board[0][0], "|", board[1][0], "|", board[2][0], "|\n" + ("-" * 17))
    print("| 1 |", board[0][1], "|", board[1][1], "|", board[2][1], "|\n" + ("-" * 17))
    print("| 2 |", board[0][2], "|", board[1][2], "|", board[2][2], "|\n" + ("-" * 17))


def print_initial_board():   # Initializes and Prints Board

    print(("-"*17) + "\n|R/C| 0 | 1 | 2 |\n" + ("-"*17) + "\n| 0 |   |   |   |\n", end="")
    print(("-" * 17) + "\n| 1 |   |   |   |\n" + ("-" * 17) + "\n| 2 |   |   |   |\n" + "-"*17)
    board = [[' ' for i in range(3)] for j in range(3)]
    return board


def check_space(board, coords):
    row, col = int(coords[0]), int(coords[2])   # Checks the space to make sure it is open
    try:
        if board[col][row] != " ":
            return 0
    except IndexError:
        return -1
    else:
        return 1


def insert_chip(board, col, row, chip_type):    # Inserts chip at the given index
    if chip_type == "x":
        board[col][row] = "X"
    elif chip_type == "o":
        board[col][row] = "O"
    return board


def check_if_winner(board, col, row, chip_type):
    counter = 0
    counter2 = 0
    if chip_type == 'x':
        for i in range(len(board)):
            counter = 0
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    counter += 1
                elif board[i][j] != 'X':
                    counter = 0
                if counter == 3:
                    return True
        for i in range(len(board)):     # Checking if X's wins
            if board[i][col] == 'X':
                counter2 += 1
            elif board[i][col] != 'X':
                counter2 = 0
            if counter2 == 3:
                return True
        counter = 0
        counter2 = 0
    elif chip_type == 'o':
        for i in range(len(board)):
            counter = 0
            for j in range(len(board[i])):
                if board[i][j] == 'o':
                    counter += 1
                elif board[i][j] != 'o':
                    counter = 0
                if counter == 3:
                    return True
        for i in range(len(board)):  # Checking if O's Wins
            if board[i][col] == 'o':
                counter2 += 1
            elif board[i][col] != 'o':
                counter2 = 0
            if counter2 == 3:
                return True

    return 0


def main():
    winner = False
    player_one_token = "x"      # Variable Definition
    player_two_token = "o"
    space_counter = 0
    total_spaces = 9
    answer = "y"

    while answer == "y":
        print("New Game: X goes first.")
        board = print_initial_board()  # Board Initialization
        while (not winner) and (space_counter <= total_spaces):

            allowed_space = -3

            while allowed_space != 1:
                coords = input("X's turn.\nWhere do you want your X placed?\nPlease enter row number and column number separated by a space.\n\n")
                print("You have entered row #" + coords[0] + "\n\t\t  and column #" + coords[2])
                allowed_space = check_space(board, coords)
                if allowed_space == -1:
                    print("Invalid entry: try again.\nRow & column numbers must be either 0, 1, or 2.\n")   # Input Validation
                    continue
                elif allowed_space == 0:
                    print("That cell is already taken.\nPlease make another selection.\n")
                    continue
                elif allowed_space == 1:
                    print("Thank you for your selection.")
                    break

            row = int(coords[0])
            col = int(coords[2])

            board = insert_chip(board, col, row, player_one_token)
            winner = check_if_winner(board, col, row, player_one_token)
            if winner is True:
                playerWin = "X"  # Stops loop if X's wins
                print(f"{playerWin} IS THE WINNER!!!")
                print_board(board)
                break
            elif space_counter == total_spaces-1:
                print("There are no winners.")
                print_board(board)
                break
            else:
                space_counter += 1
                print_board(board)

            allowed_space = -3

            while allowed_space != 1:
                coords2 = input("O's turn.\nWhere do you want your O placed?\nPlease enter row number and column number separated by a space.\n\n")
                print("You have entered row #" + coords2[0] + "\n\t\t  and column #" + coords2[2])
                allowed_space = check_space(board, coords2)
                if allowed_space == -1:
                    print("Invalid entry: try again.\nRow & column numbers must be either 0, 1, or 2.\n")
                    continue
                elif allowed_space == 0:
                    print("That cell is already taken.\nPlease make another selection.\n")
                    continue
                elif allowed_space == 1:
                    print("Thank you for your selection.")
                    break

            row2 = int(coords2[0])
            col2 = int(coords2[2])

            board = insert_chip(board, col2, row2, player_two_token)
            winner = check_if_winner(board, col2, row2, player_two_token)
            if winner is True:
                playerWin = "O"
                print(f"{playerWin} IS THE WINNER!!!")  # Stops loop if O's wins
                print_board(board)
                break
            elif space_counter == total_spaces:
                print("Draw. There are no winners.")
                print_board(board)
                break
            else:
                space_counter += 1
                print_board(board)

        answer = input("Another game? Enter Y or y for yes. ")
        answer = answer.lower()
        if answer == "y":
            winner = False
            space_counter = 0
        else:
            break


if __name__ == '__main__':
    main()
