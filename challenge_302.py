'''
This problem was asked by Uber.

You are given a 2-d matrix where each cell consists of either /, \, or an empty space.
Write an algorithm that determines into how many regions the slashes divide the space.

For example, suppose the input for a three-by-six grid is the following:

\    /
 \  /
  \/

Considering the edges of the matrix as boundaries, this divides the grid into three triangles, so you should return 3.
'''

from typing import NamedTuple
from random import choice

class Coord(NamedTuple):
    x: int
    y: int

def countRegions(matrix: list[list[str]]) -> int:
    def rCountRegions(dimensions: Coord, position: Coord, uncounted_spaces: set[Coord]):
        # When current position already counted or not empty, return.
        if position not in uncounted_spaces:
            return
        # Remove current position from the set.
        uncounted_spaces.remove(position)
        # Recur into adjacent positions.
        if position.x > 0:
            rCountRegions(dimensions, Coord(position.x-1, position.y), uncounted_spaces)
        if position.x < dimensions.x-1:
            rCountRegions(dimensions, Coord(position.x+1, position.y), uncounted_spaces)
        if position.y > 0:
            rCountRegions(dimensions, Coord(position.x, position.y-1), uncounted_spaces)
        if position.y < dimensions.y-1:
            rCountRegions(dimensions, Coord(position.x, position.y+1), uncounted_spaces)
        
        return
    
    # Get set of blank coordinates.
    uncounted_spaces = set()
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            # Assume all coordinates that are not '\' or '/' are blank.
            if not matrix[y][x] or matrix[y][x] not in "\\/":
                uncounted_spaces.add(Coord(x, y))

    region_count = 0
    while uncounted_spaces:
        rCountRegions(Coord(len(matrix[0]), len(matrix)), choice(list(uncounted_spaces)), uncounted_spaces)
        region_count += 1

    return region_count

def normalizeMatrix(matrix: list[list[str]]):
    max_len = max(map(lambda row: len(row), matrix))
    for row in matrix:
        row.extend([''] * (max_len - len(row)))
    return

if __name__ == "__main__":
    matrix = [
        ['\\', '', '', '', '', '/'],
        ['', '\\', '', '', '/', ''],
        ['', '', '\\', '/', '', '']
    ]

    print(countRegions(matrix)) # 3