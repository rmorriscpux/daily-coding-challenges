'''
A fixed point in an array is an element whose value is equal to its index.
Given a sorted array of distinct elements, return a fixed point, if one exists. Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.
'''

from typing import List

def findFixedPoint(int_list: List[int]):
    # Assuming list is pre-sorted and elements are unique, per the problem framing.
    lo, hi = 0, len(int_list)
    # Binary search looking for an element value equal to its index in the list.
    while lo < hi:
        pivot = (hi - lo) // 2 + lo
        if int_list[pivot] < pivot:
            lo = pivot + 1
        elif int_list[pivot] > pivot:
            hi = pivot
        else: # int_list[pivot] == pivot
            return pivot
    # Fixed point not found.
    return False

print(findFixedPoint([-6, 0, 2, 40]))
print(findFixedPoint([1, 5, 7, 8]))