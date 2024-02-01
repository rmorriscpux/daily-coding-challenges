'''
In linear algebra, a Toeplitz matrix is one in which the elements on any given diagonal from top left to bottom right are identical.

Here is an example:

1 2 3 4 8
5 1 2 3 4
4 5 1 2 3
7 4 5 1 2
Write a program to determine whether a given input is a Toeplitz matrix.
'''

def isToeplitz(matrix: list[list[int]]) -> bool:
    def checkDiagonal(matrix: list[list[int]], x: int, y: int, cols: int, rows: int) -> bool:
        value = matrix[y][x]
        # Backward
        i, j = x-1, y-1
        while i >=0 and j >= 0:
            if matrix[j][i] != value:
                return False
            i -= 1
            j -= 1
        # Forward
        i, j = x+1, y+1
        while i < cols and j < rows:
            if matrix[j][i] != value:
                return False
            i += 1
            j += 1
        # All equal if we get here.
        return True
    
    if not matrix:
        return False
    try:
        M, N = len(matrix[0]), len(matrix)
    except TypeError:
        return False
    # Test for complete matrix.
    if not all(map(lambda row: len(row) == M, matrix[1:])):
        return False
    # Compare every diagonal, going off the top row and leftmost column.
    for i in range(M):
        if not checkDiagonal(matrix, i, 0, M, N):
            return False
    for i in range(1, N):
        if not checkDiagonal(matrix, 0, i, M, N):
            return False
    # All equal if we get here.
    return True

if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4, 8],
        [5, 1, 2, 3, 4],
        [4, 5, 1, 2, 3],
        [7, 4, 5, 1, 2]
    ]

    print(isToeplitz(matrix))
    matrix[3][1] = 0
    print(isToeplitz(matrix))