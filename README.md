# Tic Tac Toe Game

#### By: Fares Yusuf

## Table of Contents

1. [Description](#description)
2. [Features](#features)
3. [Installation and Setup](#installation-and-setup)
4. [How to Play](#how-to-play)
5. [Contributing](#contributing)
6. [MIT License](#MIT-License)

## Description

This project is a Python-based implementation of the classic game of Tic Tac Toe, featuring a graphical user interface (GUI) built using the Pygame library. The game pits the player (X) against an AI opponent (O).

The AI opponent in this game uses the Minimax algorithm to determine its moves. The Minimax algorithm is a recursive algorithm used for decision making in game theory and artificial intelligence.

Here's how it works:

- The algorithm creates a tree of all possible game states, starting from the current state and extending to each possible future move, continuing until it reaches a state where the game is over (either one player has won, or it's a tie).
- Each end game state has a value: winning is +1, losing is -1, and a tie is 0. These values are determined from the perspective of the AI.
- The AI will then go through the tree to find the move that leads to the highest value when it's the AI's turn (maximizing player), and the lowest value when it's the human player's turn (minimizing player). This is done recursively.
- By doing this, the AI considers all possible sequences of moves and makes the most optimal move.

This implementation makes the AI a challenging opponent, as it always makes the optimal move. Enjoy testing your Tic Tac Toe skills against it!

## Features

- Player (X) vs Computer (O) gameplay.
- Graphical user interface using Pygame.
- AI opponent using Minimax algorithm.

## Installation and Setup

1. Ensure you have [Python](https://www.python.org/downloads/) installed on your machine.
2. Install Pygame by running `pip install pygame` in your command line.
3. Clone this repository to your local machine.
4. Navigate to the directory where you cloned the repo and run `python main.py` to start the game.

## How to Play

- The game board consists of a 3x3 grid. You are 'X' and the computer is 'O'.
- Players take turns placing their symbol on the grid, with the goal being to get three of their symbols in a row.
- The game ends when one player has three in a row, horizontally, vertically, or diagonally, or when all squares are filled and no player has won.

## MIT License

Copyright (c) [2023] [Fares-Yusuf]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
