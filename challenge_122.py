'''
You are given a 2-d matrix where each cell represents number of coins in that cell.
Assuming we start at matrix[0][0], and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1

The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.
'''

from typing import List

def collectCoins(board: List[List[int]]):
    def rCollectCoins(board, y, x, height, width, collected):
        if y == height-1 and x == width-1:
            # End case - Lower right corner.
            return collected + board[y][x]
        else:
            # Get outcomes for moving down and for moving right, if able.
            outcomes = []
            if y < height-1:
                outcomes.append(rCollectCoins(board, y+1, x, height, width, collected + board[y][x]))
            if x < width-1:
                outcomes.append(rCollectCoins(board, y, x+1, height, width, collected + board[y][x]))
            return max(outcomes)

    return rCollectCoins(board, 0, 0, len(board), len(board[0]), 0)

board = [
    [0, 3, 1, 1],
    [2, 0, 0, 4],
    [1, 5, 3, 1],
]

print(collectCoins(board))

board2 = [
    [0, -3, -1, -1],
    [-2, 0, 0, -4],
    [-1, -5, -3, -1],
]

print(collectCoins(board2))