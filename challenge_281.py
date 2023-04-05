'''
A wall consists of several rows of bricks of various integer lengths and uniform height.
Your goal is to find a vertical line going from the top to the bottom of the wall that cuts through the fewest number of bricks.
If the line goes through the edge between two bricks, this does not count as a cut.

For example, suppose the input is as follows, where values in each row represent the lengths of bricks in that row:

[[3, 5, 1, 1],
 [2, 3, 3, 2],
 [5, 5],
 [4, 4, 2],
 [1, 3, 3, 3],
 [1, 1, 6, 1, 1]]
The best we can we do here is to draw a line after the eighth brick, which will only require cutting through the bricks in the third and fifth row.

Given an input consisting of brick lengths for each row such as the one above, return the fewest number of bricks that must be cut to create a vertical line.
'''

# Input parameters:
# 1) List of lists (rows) containing all positive integers.
# 2) The sum of each row is equal.

from typing import List

def wallCut(wall: List[List[int]]) -> int:
    # Collect the locations on the horizontal axis where brick edges are, not counting the beginning and ending locations.
    edge_hist = {}
    for row in wall:
        cur_width = 0
        for i in range(0, len(row)-1):
            cur_width += row[i]
            if cur_width not in edge_hist:
                edge_hist[cur_width] = 0
            edge_hist[cur_width] += 1
    # Case where the wall is a singular column of bricks. edge_hist is empty.
    if not edge_hist:
        return len(wall)
    # The cut will be at the location where the most rows have an edge.
    return len(wall) - max(edge_hist.values())

wall = [
    [3, 5, 1, 1],
    [2, 3, 3, 2],
    [5, 5],
    [4, 4, 2],
    [1, 3, 3, 3],
    [1, 1, 6, 1, 1]
]

print(wallCut(wall))