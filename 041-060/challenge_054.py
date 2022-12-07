'''
Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits.
The objective is to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

Implement an efficient sudoku solver.
'''

from typing import List

# Unfilled locations represented by 0

def sudokuSolver(board: List[List[int]]):
    # Quick function to get box coordinates for use in the box_fills dictionary.
    def boxCoords(x, y):
        box_row = x - (x % 3)
        box_col = y - (y % 3)
        return "{}-{}".format(box_row, box_col)

    # Backtracking recursive subroutine. As we go through, we want to keep track of which numbers are in each row, column, and box.
    def rSudokuSolver(board, row_fills, col_fills, box_fills):
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == 0:
                    box_key = boxCoords(i, j)
                    for val in range(1, 10):
                        # Check if val (1 through 9) is not in the same row, column, or box.
                        if (val not in row_fills[i] and
                            val not in col_fills[j] and
                            val not in box_fills[box_key]):
                            board[i][j] = val
                            row_fills[i].add(val)
                            col_fills[j].add(val)
                            box_fills[box_key].add(val)
                            # Now check the recursive, and backtrack if we can't make a valid solution.
                            if rSudokuSolver(board, row_fills, col_fills, box_fills):
                                return True
                            else:
                                board[i][j] = 0
                                row_fills[i].remove(val)
                                col_fills[j].remove(val)
                                box_fills[box_key].remove(val)
                    # At this point, no valid solutions can be made from the board given.
                    return False
        # At this point, the board is complete.
        return True

    # Set up dictionaries for row, col, and box sets
    row_fills = dict()
    col_fills = dict()
    box_fills = dict()

    for i in range(0, 9):
        row_fills[i] = set()
        col_fills[i] = set()
        box_fills['{}-{}'.format(i//3*3, i%3*3)] = set()

    # Fill in the sets with already filled values.
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] != 0:
                row_fills[i].add(board[i][j])
                col_fills[j].add(board[i][j])
                box_fills[boxCoords(i, j)].add(board[i][j])

    # Now that we're set up, go through recursive function.
    rSudokuSolver(board, row_fills, col_fills, box_fills)

def printSudoku(board: List[List[int]]):
    print("|-----+-----+-----|")
    for i, row in enumerate(board):
        out_line = "|"
        for j, digit in enumerate(row):
            out_line = out_line + str(digit)
            if j % 3 == 2:
                out_line = out_line + "|"
            else:
                out_line = out_line + " "
        print(out_line)
        if i % 3 == 2:
            print("|-----+-----+-----|")

if __name__ == "__main__":
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    sudokuSolver(board)

    printSudoku(board)