'''
Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
'''

from typing import List, Tuple

def countIslands(matrix: List[List[int]]):
    # Recursive function to build out an island. Will mark an entire island as traversed and return 1 at the top level.
    def rCountIslands(matrix: List[List[int]], coords: Tuple[int, int], traversed: List[List[bool]]):
        y, x = coords

        traversed[y][x] = True

        # West
        if x > 0 and matrix[y][x-1] == 1 and not traversed[y][x-1]:
            rCountIslands(matrix, (y, x-1), traversed)
        # Southwest
        if x > 0 and y < len(matrix)-1 and matrix[y+1][x-1] == 1 and not traversed[y+1][x-1]:
            rCountIslands(matrix, (y+1, x-1), traversed)
        # South
        if y < len(matrix)-1 and matrix[y+1][x] == 1 and not traversed[y+1][x]:
            rCountIslands(matrix, (y+1, x), traversed)
        # Southeast
        if x < len(matrix[0])-1 and y < len(matrix)-1 and matrix[y+1][x+1] == 1 and not traversed[y+1][x+1]:
            rCountIslands(matrix, (y+1, x+1), traversed)
        # East
        if x < len(matrix[0])-1 and matrix[y][x+1] == 1 and not traversed[y][x+1]:
            rCountIslands(matrix, (y, x+1), traversed)
        # Northeast
        if x < len(matrix[0])-1 and y > 0 and matrix[y-1][x+1] == 1 and not traversed[y-1][x+1]:
            rCountIslands(matrix, (y-1, x+1), traversed)
        # North
        if y > 0 and matrix[y-1][x] == 1 and not traversed[y-1][x]:
            rCountIslands(matrix, (y-1, x), traversed)
        # Northwest
        if x > 0 and y > 0 and matrix[y-1][x-1] == 1 and not traversed[y-1][x-1]:
            rCountIslands(matrix, (y-1, x-1), traversed)

        return 1

    # Setup all False traversed matrix and a count of 0.
    traversed = [[False for x in range(0, len(matrix[0]))] for y in range(0, len(matrix))]
    count = 0
    # Traverse through the matrix.
    for y in range(0, len(matrix)):
        for x in range(0, len(matrix[0])):
            if not traversed[y][x]:
                if matrix[y][x] == 1:
                    count += rCountIslands(matrix, (y, x), traversed)
                traversed[y][x] = True

    return count

island_map = [
    [1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
]

print(countIslands(island_map))

island_map_2 = [
    [0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
]

print(countIslands(island_map_2))