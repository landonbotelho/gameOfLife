# Conway's Game of Life

A simple Python implementation of Conway's Game of Life. The program generates a random grid of living and dead cells and simulates how the population evolves over a specified number of iterations.

## Rules

Each cell is either **alive (1)** or **dead (0)**. Its next state is determined by its eight neighboring cells:

1. **Underpopulation:** A living cell with fewer than 2 living neighbors dies.
2. **Survival:** A living cell with 2 or 3 living neighbors survives.
3. **Overpopulation:** A living cell with more than 3 living neighbors dies.
4. **Reproduction:** A dead cell with exactly 3 living neighbors becomes alive.

All cells update simultaneously after each iteration.

## Usage

Call the `start()` function with the desired number of rows, columns, and iterations:
start(rows, columns, iterations)

Example:
start(5, 5, 8)

This generates a random 5 × 5 grid and simulates 8 iterations of the game.
