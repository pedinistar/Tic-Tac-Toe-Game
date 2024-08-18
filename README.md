# 🕹️ Tic Tac Toe Game with Python

Welcome to the **Tic Tac Toe Game** built with Python! This project is a text-based version of the classic Tic Tac Toe game, playable directly in the command line. The game features a player vs. computer mode with ASCII art, emojis, and clear instructions.

<p align="center">
  <img src="https://media.istockphoto.com/id/1365567894/vector/hand-drawn-vector-tic-tac-toe-game-noughts-and-crosses-doodle-sketch.jpg?s=612x612&w=0&k=20&c=pSs72urXBp6V8pnXvuJIfX3krtUoFhHaX6fG2g1PxUQ=" width="50%">
</p>


## 🎮 Game Overview

This is a simple Tic Tac Toe game where you play as **"X"** against the computer, which plays as **"O"**. The game alternates turns between you and the computer until there’s a winner or the game ends in a tie.

## 🛠️ Features

- **Player vs. Computer**: Play against a computer bot that makes random moves.
- **ASCII Art & Emojis**: Enjoy a visually pleasing game experience with fun ASCII art and emojis.
- **Win & Tie Detection**: The game checks for horizontal, vertical, and diagonal wins as well as ties.

## 🖥️ How to Run the Game

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/pedinistar/Tic-Tac-Toe-Game.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd tic-tac-toe-python
   ```
3. **Run the Game**:
   ```bash
   python main.py
   ```

## 🎲 How to Play

1. **Game Start**:
   - The game begins with a welcome message displayed in ASCII art.
   - You will always play as **"X"** and take the first move.

2. **Making a Move**:
   - When prompted, enter a number between `1-9` corresponding to the position on the board.
   - The board positions are mapped as follows:
     ```
      1 | 2 | 3
     -----------
      4 | 5 | 6
     -----------
      7 | 8 | 9
     ```
   - Your chosen position will be marked with **"X"**.

3. **Computer's Move**:
   - The computer will randomly select an empty spot on the board to place **"O"**.

4. **Win or Tie**:
   - The game will continue until there is a winner or a tie.
   - A win is determined when three of the same marks are in a horizontal, vertical, or diagonal row.
   - If all spots are filled without a winner, the game ends in a tie.

## 🏆 Game Logic

The game checks for a winner or a tie after each move. The logic is handled through several functions:

- **`check_horizontal()`**: Checks for a win across horizontal rows.
- **`check_vertically()`**: Checks for a win down vertical columns.
- **`check_diagonals()`**: Checks for a win along diagonals.
- **`check_tie()`**: Determines if the game is a tie when all spots are filled.

## 🤖 Computer Bot

The computer bot randomly selects an available spot on the board to place **"O"**. The bot only plays when it is the computer's turn.

## 🌟 Example Gameplay

```
  _____   _         _____   _____   _____           _____    ____  
 |_   _| | |       |_   _| |  ___| |  _  |         |  _  |  /  __| 
   | |   | |__       | |   | |___  | |_| |  ____   | |_| |  | |__  
   | |   | '_ \      | |   |  ___| |  _  / |____|  |  _  /  \___ \ 
   | |   | | | |    _| |_  | |___  | | \ \         | | \ \   ___| | 
   |_|   |_| |_|   |_____| |_____| |_|  \_\        |_|  \_\ |_____/ 

Choose the position (1-9): 5
   X   |   -   |   -   
-------|-------|-------
   -   |   X   |   -   
-------|-------|-------
   -   |   -   |   X   
The winner is X! 🎉
```
