'''
Let A be an N by M matrix in which every row and every column is sorted.

Given i1, j1, i2, and j2, compute the number of elements of A smaller than A[i1, j1] and larger than A[i2, j2].

For example, given the following matrix:

[[1, 3, 7, 10, 15, 20],
 [2, 6, 9, 14, 22, 25],
 [3, 8, 10, 15, 25, 30],
 [10, 11, 12, 23, 30, 35],
 [20, 25, 30, 35, 40, 45]]

And i1 = 1, j1 = 1, i2 = 3, j2 = 3, return 14 as there are 14 numbers in the matrix smaller than 6 or greater than 23.
'''

# Problem was modified from the email for clarity; there were some inconsistencies in it.

from typing import List

def getNumsBetween(A: List[List[int]], i1: int, j1: int, i2: int, j2: int):
    N = len(A)
    M = len(A[0])
    assert all(map(lambda row: len(row) == M, A[1:]))
    assert i1 >= 0 and i1 < N and j1 >= 0 and j1 < M and i2 >= 0 and i2 < N and j2 >= 0 and j2 < M

    if A[i1][j1] == A[i2][j2]:
        num_instances = 0
        for row in A:
            num_instances += row.count(A[i1][j1])
        count = N * M - num_instances

    elif A[i1][j1] > A[i2][j2]:
        count = N * M

    else:
        count = 0
        for row in A[:i1]:
            count += list(map(lambda num: num < A[i1][j1], row)).count(True)
        for row in A[i1:]:
            count += list(map(lambda num: num < A[i1][j1], row[:j1])).count(True)
        for row in A[i2+1:]:
            count += list(map(lambda num: num > A[i2][j2], row)).count(True)
        for row in A[:i2+1]:
            count += list(map(lambda num: num > A[i2][j2], row[j2+1:])).count(True)

    return count

matrix = [
    [1, 3, 7, 10, 15, 20],
    [2, 6, 9, 14, 22, 25],
    [3, 8, 10, 15, 25, 30],
    [10, 11, 12, 23, 30, 35],
    [20, 25, 30, 35, 40, 45]
]

print(getNumsBetween(matrix, 1, 1, 3, 3))
print(getNumsBetween(matrix, 2, 4, 4, 1))