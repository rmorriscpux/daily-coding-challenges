'''
Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

For example, for the input [1, 2, 3, 10], you should return 7.

Do this in O(N) time.
'''

from typing import List
from bisect import bisect

def smallestNonSum(int_arr: List[int]):
    # Include only positive integers.
    start = bisect(int_arr, 0)
    max_sum = 1
    for num in int_arr[start:]:
        if num > max_sum:
            break
        max_sum += num
    return max_sum