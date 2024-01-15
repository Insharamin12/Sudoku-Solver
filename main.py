class Board:
    def __init__(self, board):
        self.board = board

    def __str__(self):
        upper_lines = f'\n╔═══{"╤═══"*2}{"╦═══"}{"╤═══"*2}{"╦═══"}{"╤═══"*2}╗\n'
        middle_lines = f'╟───{"┼───"*2}{"╫───"}{"┼───"*2}{"╫───"}{"┼───"*2}╢\n'
        lower_lines = f'╚═══{"╧═══"*2}{"╩═══"}{"╧═══"*2}{"╩═══"}{"╧═══"*2}╝\n'
        board_string = upper_lines

         # Iterate through each row of the board
        for index, line in enumerate(self.board):
            row_list = []
             # Iterate through each group of three squares in the row
            for square_no, part in enumerate([line[:3], line[3:6], line[6:]], start=1):
                row_square = "|".join(str(item) for item in part)
                row_list.extend(row_square)
                if square_no != 3:
                    row_list.append("║")

            row = f'║ {" ".join(row_list)} ║\n'
            row_empty = row.replace("0", " ") # Replace '0' with a space for empty cells
            board_string += row_empty
            
            # Add horizontal lines after every three rows
            if index < 8:
                if index % 3 == 2:
                    board_string += (
                        f'╠═══{"╪═══"*2}{"╬═══"}{"╪═══"*2}{"╬═══"}{"╪═══"*2}╣\n'
                    )
                else:
                    board_string += middle_lines
            else:
                board_string += lower_lines

        return board_string

    # Find the first empty cell in the board
    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None

    # Check if a number is valid to be placed in a certain row
    def valid_in_row(self, row, num):
        return num not in self.board[row]

    # Check if a number is valid to be placed in a certain column
    def valid_in_col(self, col, num):
        return all(self.board[row][col] != num for row in range(9))

    # Check if a number is valid to be placed in a certain 3x3 square
    def valid_in_square(self, row, col, num):
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty, num):
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        return all([valid_in_row, valid_in_col, valid_in_square])

    # Solve the Sudoku puzzle using backtracking
    def solver(self):
        if (next_empty := self.find_empty_cell()) is None:
            return True
        else:
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    if self.solver():
                        return True
                    self.board[row][col] = 0

        return False

# Function to solve Sudoku puzzle
def solve_sudoku(board):
    gameboard = Board(board)
    print(f"\nPuzzle to solve:\n{gameboard}")
    if gameboard.solver():
        print("\nSolved puzzle:")
        print(gameboard)

    else:
        print("\nThe provided puzzle is unsolvable.")
    return gameboard


puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]
solve_sudoku(puzzle)
