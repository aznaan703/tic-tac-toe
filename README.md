
# Tic-Tac-Toe Game

A simple Tic-Tac-Toe game created using Python and Pygame. Play against another player on the same computer!

## Features

- Playable 3x3 grid.
- Player 1 uses circles, Player 2 uses crosses.
- Win detection for rows, columns, and diagonals.
- Restart the game with the 'R' key.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/aznaan703/tic-tac-toe.git
   cd tic-tac-toe
   ```

2. **Install Pygame:**

   ```bash
   pip install pygame
   ```

## Running the Game

Run the game with:

```bash
python tic_tac_toe.py
```

## How to Play

- Click on a square to place your mark (circle or cross).
- The game will automatically detect and announce a win.
- Press 'R' to restart the game after a win.

## Code Overview

- **`create_lines()`**: Draws the grid lines.
- **`draw_figures()`**: Draws circles and crosses on the board.
- **`mark_square(row, col, player)`**: Marks a square with the player's symbol.
- **`available_square(row, col)`**: Checks if a square is empty.
- **`is_board_full()`**: Checks if the board is full.
- **`check_win(player)`**: Checks if the player has won.
- **`restart()`**: Resets the game.

## Contributing

Feel free to fork the repository and submit pull requests. Please ensure your changes are well-documented.

---

