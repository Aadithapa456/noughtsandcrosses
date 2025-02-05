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
    # develop code to draw the board
    for row in board:
        print("-----------------".center(22))
        for cell in row:
            print(f" | {cell} |", end=" ")
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
    for row in range(len(board)):
        for column in range(len(board[row])):
            board[row][column] = " "
    return board


def get_player_move(board, user_moves):
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
            grouped_moves = []
            row, col = rows_cols[int(player_move)]
            if board[row][col] == " ":
                user_moves.append([row, col])
            # Grouping matched moves by comparing with win_pattern
            for pattern in win_pattern:
                matched = []
                for move in user_moves:
                    if move in pattern:
                        matched.append(move)
                if len(matched) > 0:
                    grouped_moves.append(matched)
            else:
                print("Cell is already occupied! Try again.")
            break
    return row, col, grouped_moves


def choose_computer_move(board, user_moves):
    # Your custom move logic goes here
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
        highest_length_list = [val for val in user_moves if len(val) > 1]
        req = []
        if highest_length_list:
            # Extracting the latest addition
            highest_length = highest_length_list[-1]
            highest_length_list.pop()
        else:
            highest_length = []
        if highest_length:
            for pattern in win_pattern:
                match_count = 0
                for move in highest_length:
                    if move in pattern:
                        match_count += 1
                if match_count >= 2:
                    req = pattern
                    break
            difference = (
                [item for item in req if item not in highest_length] if req else []
            )
            print("Difference", difference)
            if difference:
                # Iterate over the difference list until an empty candidate is found.
                candidate_found = False
                while difference:
                    candidate = difference[0]
                    print("Candidate", candidate)
                    r, c = candidate
                    if board[r][c] == " ":
                        row, col = candidate
                        candidate_found = True
                        break
                    else:
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
    # develop code to check if either the player or the computer has won
    # return True if someone won, False otherwise
    for i in range(len(board)):
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
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise
    for row in board:
        if " " in row:
            return False
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
    user_moves = []
    while True:
        # Player's move
        player_row, player_col, grouped_moves = get_player_move(board, user_moves)
        board[player_row][player_col] = "X"
        draw_board(board)
        if check_for_win(board, "X"):
            return 1
        if check_for_draw(board):
            return 0
        computer_row, computer_col = choose_computer_move(board, grouped_moves)
        board[computer_row][computer_col] = "O"
        draw_board(board)
        if check_for_win(board, "O"):
            return -1
        if check_for_draw(board):
            return 0


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
    try:
        with open("leaderboard.txt", "r") as f:
            leaders = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        leaders = {}
    return leaders


def save_score(score):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    player_name = input("Enter your name: ")
    existing_players = load_scores()
    if player_name in existing_players:
        existing_players[player_name] += score
    else:
        existing_players[player_name] = score
    with open("leaderboard.txt", "w") as f:
        json.dump(existing_players, f)
    print("Saved")
    return


def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader
    print("Shown")
    for player, score in sorted(
        leaders.items(), key=lambda item: item[1], reverse=True
    ):
        print(f"{player}: {score}")
    pass
