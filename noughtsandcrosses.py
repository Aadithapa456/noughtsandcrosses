"""
Imports the necessary modules for the game.

Modules:
    - random: Used to generate random numbers.
    - os.path: Provides functions for interacting with the operating system's file system
    - json: Enables reading and writing data in JSON format, 
            used for storing and retrieving the leaderboard.
"""

import random
import os.path
import json

random.seed()
win_pattern = [
    [[0, 0], [0, 1], [0, 2]],  # Row 1
    [[1, 0], [1, 1], [1, 2]],  # Row 2
    [[2, 0], [2, 1], [2, 2]],  # Row 3
    [[0, 0], [1, 0], [2, 0]],  # Column 1
    [[0, 1], [1, 1], [2, 1]],  # Column 2
    [[0, 2], [1, 2], [2, 2]],  # Column 3
    [[0, 0], [1, 1], [2, 2]],  # Diagonal 1
    [[0, 2], [1, 1], [2, 0]],  # Diagonal 2
]


def draw_board(board):
    """
    This function takes a noughts and crosses board represented by a 2D list and prints it
    in a formatted manner.
    Params:
        board (list): A 2D list where each sublist represents a row of the
        board and each element in the sublist represents a cell which can be 'X', 'O', or ' '.
    Return:
        None
    """
    for row in board:
        print(("-" * 18).center(22))
        for cell in row:
            print(f"  | {cell} |", end="")
        print("")
    print(("-" * 18).center(22))


def welcome(board):
    """
    This function prints a welcome message and displays the current state of the board.
    Params:
        board (list): A 2D list representing the current state of the game board.
    Return:
        None
    """

    print('Welcome to the "Unbeatable Noughts and Crosses" game.')
    print("The board layout is shown below:")
    draw_board(board)
    print("When prompted, enter the number corresponding to the square you want")


def initialise_board(board):
    """
    This function sets all elements of the given board to a single space ' '.
    Params:
        board (list): A 2D list representing the game board.
    Return:
        list: The modified board with all elements set to ' '.
    """

    for row_index, row in enumerate(board):
        for col_index, _ in enumerate(row):
            board[row_index][col_index] = " "
    return board


def get_player_move(board):
    """
    This function prompts the user to select a cell on the board to place their
    'X' in a game of noughts and crosses.
    Params:
        board (list): The current state of the game board, represented as a 2D list.
    Return:
        tuple: A tuple containing the row and column indices of the selected cell.
    """

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
    row, col = [0, 0]
    while True:
        print((" " * 19), "1 2 3")
        print((" " * 19), "4 5 6")
        player_move = input("Choose your square: 7 8 9 :")
        if player_move.isalpha():
            print("Invalid Selection")
        elif player_move not in "123456789":
            print("Invalid Move")
        else:
            row, col = rows_cols[int(player_move)]
        if board[row][col] == " ":
            user_moves.append([row, col])
            for pattern in win_pattern:
                matched = []
                for move in user_moves:
                    if move in pattern:
                        matched.append(move)
                if len(matched) > 0:
                    grouped_moves.append(matched)
            break
        else:
            print("Cell is already occupied! Try again.")
    return row, col


def choose_computer_move(board):
    """
    This function determines the computer's move in a game of noughts and crosses
    Params:
        board (list): The current state of the game board, represented as a 2D list.
    Return:
        tuple: A tuple containing the row and column indices (row, col) of the chosen move.
    """

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
        # Tracking user's possible winning moves
        # Exctracting probable threats; 1 or more moves left to win
        highest_length_list = [val for val in grouped_moves if len(val) > 1]
        required_pattern = []
        if highest_length_list:
            # Extracting the latest addition
            highest_length = highest_length_list[-1]
            highest_length_list.pop()  # Pops out last element
        else:
            highest_length = []
        if highest_length:
            for pattern in win_pattern:
                match_count = 0
                for move in highest_length:
                    if move in pattern:
                        match_count += 1
                if match_count >= 2:
                    required_pattern = pattern
                    break
            difference = (
                [item for item in required_pattern if item not in highest_length]
                if required_pattern
                else []
            )
            if difference:
                # Iterates over the difference list until an empty candidate is found.
                candidate_found = False
                while difference:
                    candidate = difference[0]
                    r, c = candidate
                    if board[r][c] == " ":
                        row, col = candidate
                        candidate_found = True
                        break
                    difference.pop(0)  # Remove candidate if cell is not empty
                if not candidate_found:
                    random_number = random.randint(1, 9)
                    row, col = rows_cols[random_number]  # Fallback move
        else:
            random_number = random.randint(1, 9)
            row, col = rows_cols[random_number]
        if board[row][col] == " ":
            break
    return row, col


def check_for_win(board, mark):
    """
    This function checks if the given mark has won in the noughts and crosses game.
    Params:
        board (list): The current state of the game board, represented as a 2D list.
        mark (str): The mark to check for a win ('X' or 'O').
    Return:
        bool: True if the given mark has won, False if not
    """

    for i, _ in enumerate(board):
        rows_match = True
        col_match = True
        for j in range(3):
            if board[i][j] != mark:
                rows_match = False
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
    """
    This function checks if the game board is in a
    draw state by verifying if all cells are occupied.
    Params:
        board (list): The current state of the game board, represented as a 2D list.
    Return:
        bool: Returns True if all cells are occupied (indicating a draw), False if not.
    """

    for row in board:
        if " " in row:
            return False
    return True


def play_game(board):
    """
    This function plays a game of noughts and crosses (tic-tac-toe) between a
    player and the computer.
    Params:
        board (list): A 2D list where each sublist represents a row of the
        board and each element in the sublist represents a cell which can be 'X', 'O', or ' '.
    Return:
        int: The score of the game. Returns 1 if the player wins,
        -1 if the computer wins, and 0 if the game is a draw.
    """

    global user_moves, grouped_moves
    initialise_board(board)
    user_moves = []
    grouped_moves = []
    while True:
        # Player's move
        player_row, player_col = get_player_move(board)
        board[player_row][player_col] = "X"
        draw_board(board)
        if check_for_win(board, "X"):
            return 1
        if check_for_draw(board):
            return 0
        print("Computers Turn: ")
        computer_row, computer_col = choose_computer_move(board)
        board[computer_row][computer_col] = "O"
        draw_board(board)
        if check_for_win(board, "O"):
            return -1
        if check_for_draw(board):
            return 0


def menu():
    """
    This function displays a menu to the user and prompts them to select an option.
    Params:
        None
    Return:
        choice (str): The user's choice, which can be '1', '2', '3', or 'q'.
    """

    while True:
        print("Enter one of the following options:")
        print("1 - Play the game")
        print("2 - Save your score in the leaderboard")
        print("3 - Load and display the leaderboard")
        print("q - End the program")
        choice = input("1,2,3 or q?")
        if choice.isalpha():
            choice = str(choice)
        if choice not in ["1", "2", "3", "q"]:
            print("\nInvalid choice:\n")
        else:
            break
    return choice


def load_scores():
    """
    This function loads the leaderboard scores from the file 'leaderboard.txt'.
    Params:
        None
    Return:
        leaders (dict): A dictionary with player names as keys and their scores as values.
    """

    if os.path.exists("leaderboard.txt"):
        try:
            with open("leaderboard.txt", "r", encoding="utf-8") as f:
                leaders = json.load(f)
        except json.JSONDecodeError:
            leaders = {}
    else:
        leaders = {}
    return leaders


def save_score(score):
    """
    This function takes the current score and saves it to the 'leaderboard.txt'
    file under the player's name.
    Params:
        score (int): The score to be saved for the player.
    Return:
        None
    """

    player_name = input("Enter your name: ")
    existing_players = load_scores()
    if player_name in existing_players:
        existing_players[player_name] += score
    else:
        existing_players[player_name] = score
    with open("leaderboard.txt", "w", encoding="utf-8") as f:
        json.dump(existing_players, f)
    print("Saved Sucessfully!")


def display_leaderboard(leaders):
    """
    This function takes a dictionary of player names and their scores,
    and prints the leaderboard in descending order of scores.
    Params:
        leaders (dict): A dictionary where keys are player names (str)
                        and values are their scores (int).
    Return:
        None
    """

    print("\nLeaderboard:\n")
    for rank, (player, score) in enumerate(leaders.items(), start=1):
        point_or_points = "Points" if score > 1 else "Point"
        print(f"{rank}.{player} : {score} {point_or_points}")
    print(" ")
