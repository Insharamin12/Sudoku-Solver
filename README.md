# Sudoku-Solver

### Classes and objects are important programming concepts. In Python, a class is a blueprint for creating objects. Objects created from a class are instances of that class. 

**Below is a brief overview of the provided code:**

## Class: Board
The Board class represents the Sudoku puzzle board. It includes methods for checking the validity of numbers in rows, columns, and 3x3 squares. The solver method utilizes backtracking to find the solution for the puzzle.

## Methods:
- __init__(self, board): Initializes the board with the provided 9x9 puzzle.

- __str__(self): Returns a formatted string representation of the Sudoku board.

- find_empty_cell(self): Finds the first empty cell (cell with the value 0) on the board.

- valid_in_row(self, row, num): Checks if a number is valid in a specific row.

- valid_in_col(self, col, num): Checks if a number is valid in a specific column.

- valid_in_square(self, row, col, num): Checks if a number is valid in the 3x3 square containing the specified cell.

- is_valid(self, empty, num): Checks if a number is valid in the empty cell.

- solver(self): Solves the Sudoku puzzle using a backtracking algorithm.

## Function: solve_sudoku
The solve_sudoku function creates a Board instance with the provided puzzle and prints the original puzzle. It then attempts to solve the puzzle using the solver method and prints the solved puzzle or indicates if the puzzle is unsolvable.

# How It Works
1. The Sudoku solver uses a backtracking algorithm to fill in the empty cells of the puzzle.
2. The program iterates through each empty cell and attempts to fill it with a valid number (1-9) based on Sudoku rules.
3. If a valid number is found, it continues to the next empty cell. If not, it backtracks and explores other possibilities.

Feel free to use, modify, and contribute to this Sudoku solver project! Happy Sudoku solving!
