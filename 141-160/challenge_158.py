'''
You are given an N * M matrix of 0s and 1s. Starting from the top left corner, how many ways are there to reach the bottom right corner?

You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot walk through.

For example, given the following matrix:

[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]

Return 2, as there are only two ways to get to the bottom right:

    Right, down, down, right
    Down, right, down, right

The top left corner and bottom right corner will always be 0.
'''

from typing import List

def countPaths(board: List[List[int]]):
    # Recursive routine so max position values only need to be calculated one time. This optimizes for time.
    def rCountPaths(board, x, y, max_x, max_y):
        # Path completed to the bottom right corner.
        if x == max_x and y == max_y:
            return 1

        count = 0
        # Check if we can go down.
        if y < max_y and not board[y+1][x]:
            count += rCountPaths(board, x, y+1, max_x, max_y)
        # Check if we can go right.
        if x < max_x and not board[y][x+1]:
            count += rCountPaths(board, x+1, y, max_x, max_y)

        return count

    return rCountPaths(board, 0, 0, len(board[0])-1, len(board)-1)

board = [
    [0, 0, 1],
    [0, 0, 1],
    [1, 0, 0]
]

print(countPaths(board))