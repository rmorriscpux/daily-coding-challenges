'''
Given an N by M matrix consisting only of 1's and 0's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

[[1, 0, 0, 0],
 [1, 0, 1, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 0]]

Return 4.
'''

from typing import List

def getLargestRectangle(board: List[List[int]]):
    # Helper functions for comparison.
    def rowExtend(board, end_row, start_col, end_col):
        return all(board[end_row][start_col:end_col])

    def colExtend(board, end_col, start_row, end_row):
        for row in range(start_row, end_row):
            if not board[row][end_col]:
                return False
        return True

    # Recursive Check
    def rGetLargestRectangle(board, start_row, end_row, start_col, end_col):
        current_area = (end_row - start_row) * (end_col - start_col)
        row_extended_area = 0
        col_extended_area = 0

        # Check to see if we can extend the rows and columns.
        if end_row < len(board) and rowExtend(board, end_row, start_col, end_col):
            row_extended_area = rGetLargestRectangle(board, start_row, end_row+1, start_col, end_col)

        if end_col < len(board[0]) and colExtend(board, end_col, start_row, end_row):
            col_extended_area = rGetLargestRectangle(board, start_row, end_row, start_col, end_col+1)

        # Return the largest current, or if we extended rows and columns.
        return max(current_area, row_extended_area, col_extended_area)

    if not board:
        return 0

    max_area = 0

    num_rows, num_cols = len(board), len(board[0])
    for i in range(0, num_rows):
        for j in range(0, num_cols):
            upper_bound = (num_rows - i) * (num_cols - j)
            if board[i][j] and upper_bound > max_area:
                max_area = max(max_area, rGetLargestRectangle(board, i, i+1, j, j+1))

    return max_area

board = [
    [1, 0, 0, 0],
    [1, 0, 1, 1],
    [1, 0, 1, 1],
    [0, 1, 0, 0]
]

print(getLargestRectangle(board))