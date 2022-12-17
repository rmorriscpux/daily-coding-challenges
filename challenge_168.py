'''
Given an N by N matrix, rotate it by 90 degrees clockwise.

For example, given the following matrix:

[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

you should return:

[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]

Follow-up: What if you couldn't use any extra space?
'''

from typing import List

def rotateMatrix(matrix: List[list]):
    N = len(matrix)
    for row in matrix:
        assert(len(row) == N)

    for ring in range(0, N//2):
        for side_space in range(ring, N-1-ring):
            # right side = matrix[ring+side_space][N-1-ring]
            # bottom side = matrix[N-1-ring][N-1-side_space]
            # left side = matrix[N-1-side_space][ring]
            # top side = matrix[ring][side_space]
            temp = matrix[ring][side_space]
            matrix[ring][side_space] = matrix[N-1-side_space][ring]
            matrix[N-1-side_space][ring] = matrix[N-1-ring][N-1-side_space]
            matrix[N-1-ring][N-1-side_space] = matrix[ring+side_space][N-1-ring]
            matrix[ring+side_space][N-1-ring] = temp

    return

def printMatrix(matrix: List[list]):
    for row in matrix:
        print(row)
    return

num_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

printMatrix(num_matrix)
rotateMatrix(num_matrix)
print("====================")
printMatrix(num_matrix)

print("====================")
letter_matrix = [
    ['a', 'b', 'c', 'd'],
    ['e', 'f', 'g', 'h'],
    ['i', 'j', 'k', 'l'],
    ['m', 'n', 'o', 'p']
]

printMatrix(letter_matrix)
rotateMatrix(letter_matrix)
print("====================")
printMatrix(letter_matrix)