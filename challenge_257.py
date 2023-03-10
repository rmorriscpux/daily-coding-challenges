'''
Given an array of integers out of order, determine the bounds of the smallest window that must be sorted in order for the entire array to be sorted.
For example, given [3, 7, 5, 6, 9], you should return (1, 3).
'''

from typing import List, Tuple

def smallestSortWindow(int_arr: List[int]) -> Tuple[int, int]:
    sorted_arr = sorted(int_arr)
    if int_arr == sorted_arr:
        # Array already sorted.
        return (0, 0)
    
    arr_len = len(int_arr)
    # Determine the end point.
    end = 1
    while end < arr_len:
        # Increment end up until everything past end is sorted, while everything up to end is below the value at end+1.
        if sorted(int_arr[:end+1]) + int_arr[end+1:] == sorted_arr:
            break
        end += 1

    start = 0
    while start < arr_len - 1:
        # Increment start up until a point where starting past it would not result in a sorted array.
        if int_arr[:start+1] + sorted(int_arr[start+1:]) != sorted_arr:
            break
        start += 1

    return (start, end)

print(smallestSortWindow([3, 7, 5, 6, 9]))
print(smallestSortWindow([5, 4, 3, 2, 1]))
print(smallestSortWindow([1, 2, 3, 4, 5]))