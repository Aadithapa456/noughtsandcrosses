# Noughts and Crosses (Tic Tac Toe)

This is a simple implementation of the classic game Noughts and Crosses (also known as Tic Tac Toe) in Python.

## How to Play

1. Run the `play_game.py` script to start the game.
2. You will be presented with a menu:
   - Press `1` to play the game.
   - Press `2` to save your score.
   - Press `3` to load and display the leaderboard.
   - Press `q` to quit the game.

## Game Rules

- The game is played on a 3x3 grid.
- You are `X`, and the computer is `O`.
- Players take turns putting their marks in empty squares.
- The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
- If all 9 squares are full and no player has 3 marks in a row, the game is a draw.

## Files

- `main.py`: Contains some initial code for displaying the board.
- `noughtsandcrosses.py`: Contains the main game logic and functions.
- `play_game.py`: Contains the main function to run the game.
- `leaderboard.txt`: Stores the leaderboard scores.
- `.gitignore`: Specifies files to be ignored by Git.

## Functions

- `draw_board(board)`: Draws the game board.
- `welcome(board)`: Displays a welcome message and the initial board.
- `initialise_board(board)`: Initializes the game board.
- `get_player_move(board)`: Gets the player's move.
- `choose_computer_move(board)`: Chooses the computer's move.
- `check_for_win(board, mark)`: Checks if a player has won.
- `check_for_draw(board)`: Checks if the game is a draw.
- `play_game(board)`: Plays the game.
- `menu()`: Displays the menu and gets the user's choice.
- `load_scores()`: Loads the leaderboard scores from the file.
- `save_score(score)`: Saves the current score to the file.
- `display_leaderboard(leaders)`: Displays the leaderboard scores.

## Requirements

- Python 3.x

## How to Run

1. Clone the repository.
2. Navigate to the project directory.
3. Run `python play_game.py` to start the game.

Enjoy playing Noughts and Crosses!
