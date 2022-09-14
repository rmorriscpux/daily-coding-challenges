'''
Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.
'''

from typing import List

def canMakeNonDecreasing(num_arr: List[int]):
    if len(num_arr) <= 2:
        return True

    decreasing_pairs = 0

    for i in range(1, len(num_arr)):
        if num_arr[i] < num_arr[i-1]:
            decreasing_pairs += 1
        if decreasing_pairs >= 2:
            return False

    return True

print(canMakeNonDecreasing([10, 5, 7]))
print(canMakeNonDecreasing([10, 5, 1]))