'''
There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of
starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

    Right, then down
    Down, then right

Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
'''

# NOTE: The contents of the matrix are irrelevant. We're only concerned with the dimensions.
from typing import List

def countTraversals(board: List[List[int]]):

    def rCountTraversals(x, y, M, N):
        # End case: We are at the bottom right.
        if x == M-1 and y == N-1:
            return 1

        count = 0
        # Recur into valid moves, right and down.
        if x < M-1:
            count += rCountTraversals(x+1, y, M, N)
        if y < N-1:
            count += rCountTraversals(x, y+1, M, N)

        return count

    return rCountTraversals(0, 0, len(board[0]), len(board))

board1 = [[0 for i in range(2)] for j in range(2)]
board2 = [[0 for i in range(5)] for j in range(5)]

print(countTraversals(board1))
print(countTraversals(board2))