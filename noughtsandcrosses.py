import random
import os.path
import json

random.seed()


def draw_board(board):
    # develop code to draw the board
    a = [[1, 0, 0], [1, 1, 0], [0, 0, 1]]
    for i in a:
        print("-----------------".center(22))
        for j in i:
            if j == 0:
                print(f" | O |", end=" ")
            else:
                print(f" | X |", end=" ")
        print("")
    print("-----------------".center(22))
    pass


def welcome(board):
    # prints the welcome message
    # display the board by calling draw_board(board)
    draw_board(board)
    pass


def initialise_board(board):
    # develop code to set all elements of the board to one space ' '
    for row in len(board):
        for column in len(board[row]):
            board[row][column] = ""
    return board


def get_player_move(board):
    # develop code to ask the user for the cell to put the X in,
    # and return row and col
    rows_cols = {
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
        9: [2, 2],
    }
    while True:
        print("                    1 2 3")
        print("                    4 5 6")
        player_move = input("Choose your square: 7 8 9 :")
        if player_move.isalpha():
            print("Invalid Selection")
        elif player_move not in "123456789":
            print("Invalid Move")
        else:
            player_move = int(player_move)
            break
    row, col = rows_cols[player_move]
    return row, col


def choose_computer_move(board):
    # develop code to let the computer chose a cell to put a nought in
    # and return row and col
    
    return row, col


def check_for_win(board, mark):
    # develop code to check if either the player or the computer has won
    # return True if someone won, False otherwise
    for i in range(len(board)):
        rows_match = True
        col_match = True
        for j in range(3):
            if board[i][j] != mark:
                rows_match = True
                break
            if board[j][i] != mark:
                col_match = False
        if rows_match or col_match:
            return True
    main_diag = secondary_diag = True
    for i in range(3):
        if board[i][i] != mark:
            main_diag = False
        if board[i][2 - i] != mark:
            secondary_diag = False
    return main_diag or secondary_diag


def check_for_draw(board):
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise
    return True


def play_game(board):
    # develop code to play the game
    # star with a call to the initialise_board(board) function to set
    # the board cells to all single spaces ' '
    # then draw the board
    # then in a loop, get the player move, update and draw the board
    # check if the player has won by calling check_for_win(board, mark),
    # if so, return 1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    # if not, then call choose_computer_move(board)
    # to choose a move for the computer
    # update and draw the board
    # check if the computer has won by calling check_for_win(board, mark),
    # if so, return -1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    # repeat the loop
    initialise_board(board)
    player_row, player_col = get_player_move()
    board[player_row][player_col] = "X"
    draw_board(board)
    if check_for_win(board, "X"):
        return 1
    if check_for_draw(board):
        return 0
    computer_col, computer_row = choose_computer_move()


def menu():
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program
    print("Enter one of the following options:")
    print("1 - Play the game")
    print("2 - Save your score in the leaderboard")
    print("3 - Load and display the leaderboard")
    print("q - End the program")
    while True:
        choice = input("1,2,3 or q?")
        if choice.isalpha():
            choice = str(choice)
        if choice in ["1", "2", "3", "q"]:
            break
    return choice


def load_scores():
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders
    return leaders


def save_score(score):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    return


def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader
    pass
