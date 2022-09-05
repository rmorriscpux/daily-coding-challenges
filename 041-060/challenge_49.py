'''
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
'''

from typing import List

def getMaxSum(arr: List):
    # List all negative or 0
    if max(arr) <= 0:
        return 0
    # Empty List
    if not arr:
        return 0

    max_sum = temp_max_sum = arr[0]

    # Traverses the list and maintains a max sum, discarding it if a larger contiguous sum comes along.
    for num in arr[1:]:
        temp_max_sum = max(num, temp_max_sum + num)
        max_sum = max(max_sum, temp_max_sum)

    return max_sum

print(getMaxSum([34, -50, 42, 14, -5, 86]))
print(getMaxSum([-5, -1, -8, -9]))