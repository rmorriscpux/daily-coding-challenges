'''
You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers.
For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:

  1
 2 3
1 5 1
We define a path in the triangle to start at the top and go down one row at a time to an adjacent value,
eventually ending with an entry on the bottom row. For example, 1 -> 3 -> 5. The weight of the path is the sum of the entries.

Write a program that returns the weight of the maximum weight path.
'''

from typing import List

def maxPath(num_triangle: List[List[int]]):
    # IndexError raised if len(num_triangle[row]) < row + 1. Numbers in a row beyond the value of row are ignored.
    def rMaxPath(num_triangle, row, index, cur_sum):
        # At the final row.
        if row == len(num_triangle) - 1:
            return cur_sum + num_triangle[row][index]
        # Add to cur_sum and recur into the left and right sides below. 
        new_sum = cur_sum + num_triangle[row][index]
        return max(rMaxPath(num_triangle, row+1, index, new_sum), rMaxPath(num_triangle, row+1, index+1, new_sum))

    return rMaxPath(num_triangle, 0, 0, 0)

num_triangle = [
    [1],
    [2, 3],
    [1, 5, 1]
]

print(maxPath(num_triangle))