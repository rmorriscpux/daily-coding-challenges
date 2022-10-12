'''
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]

You should print out the following:

1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12
'''

def spiral(matrix):
    N = len(matrix)
    M = len(matrix[0])

    visited = [[False for j in range(M)] for i in range(N)]

    def goRight(matrix, visited, x, y, N, M, out_list):
        while True:
            visited[y][x] = True
            out_list.append(matrix[y][x])
            if x >= M-1 or visited[y][x+1]:
                break
            x += 1

        if y < N-1 and not visited[y+1][x]:
            goDown(matrix, visited, x, y+1, N, M, out_list)

    def goDown(matrix, visited, x, y, N, M, out_list):
        while True:
            visited[y][x] = True
            out_list.append(matrix[y][x])
            if y >= N-1 or visited[y+1][x]:
                break
            y += 1

        if x > 0 and not visited[y][x-1]:
            goLeft(matrix, visited, x-1, y, N, M, out_list)

    def goLeft(matrix, visited, x, y, N, M, out_list):
        while True:
            visited[y][x] = True
            out_list.append(matrix[y][x])
            if x <= 0 or visited[y][x-1]:
                break
            x -= 1

        if y > 0 and not visited[y-1][x]:
            goUp(matrix, visited, x, y-1, N, M, out_list)

    def goUp(matrix, visited, x, y, N, M, out_list):
        while True:
            visited[y][x] = True
            out_list.append(matrix[y][x])
            if y <= 0 or visited[y-1][x]:
                break
            y -= 1

        if x < M-1 and not visited[y][x+1]:
            goRight(matrix, visited, x+1, y, N, M, out_list)

    out_list = []

    goRight(matrix, visited, 0, 0, N, M, out_list)

    return out_list

matrix = [
    [1,  2,  3,  4,  5],
    [6,  7,  8,  9,  10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

print(spiral(matrix))