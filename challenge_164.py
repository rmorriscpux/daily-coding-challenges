'''
You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}.
By the pigeonhole principle, there must be a duplicate. Find it in linear time and space.
'''

from typing import List

# Interpretation: All integers in the set from 1 to n are present in the array, and the array has n + 1 elements, therefore there is exactly one duplicate in the array.

def getDuplicateInteger(int_list: List[int]):
    n = len(int_list) - 1
    # A set of numbers from 1 to n contains (n/2) instances of n + 1. So the set sum calculation can be reduced to the below.
    set_sum = (n+1) * n // 2
    # From there it's a matter of subtracting the set sum from the list sum.
    return sum(int_list) - set_sum

print(getDuplicateInteger([1, 2, 3, 4, 5, 3, 6, 7, 8, 9, 10]))