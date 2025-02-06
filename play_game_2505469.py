"""
Imports necessary functions from the noughtsandcrosses module.

Functions imported:
    - welcome: Displays a welcome message and the initial game board.
    - menu: Displays the game menu and handles user input.
    - play_game: Manages the game loop and gameplay between the player and the computer.
    - save_score: Saves the player's score to the leaderboard.
    - load_scores: Loads the leaderboard scores from a file.
    - display_leaderboard: Displays the leaderboard in descending order of scores.
"""

from noughtsandcrosses import (
    welcome,
    menu,
    play_game,
    save_score,
    load_scores,
    display_leaderboard,
)


def main():
    """
    The main function to run the "Unbeatable Noughts and Crosses" game.

    This function initializes the game board, displays a welcome message,
    and enters a loop to handle the game menu.
    The player can choose to play the game, save their score, view the leaderboard,
    or quit the game.

    Params:
        None

    Return:
        None
    """

    board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

    welcome(board)
    total_score = 0
    while True:
        choice = menu()
        if choice == "1":
            score = play_game(board)
            total_score += score
            print("Your current score is:", total_score)
        if choice == "2":
            save_score(total_score)
        if choice == "3":
            leader_board = load_scores()
            display_leaderboard(leader_board)
        if choice == "q":
            print('Thank you for playing the "Unbeatable Noughts and Crosses" game.')
            print("Good bye")
            return


# Program execution begins here
if __name__ == "__main__":
    main()
