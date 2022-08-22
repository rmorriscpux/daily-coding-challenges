'''
A sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.
'''

from typing import List

def findIndex(arr: List[int], element: int):
    if element >= arr[0]:
        for i in range(0, len(arr)):
            if arr[i] == element:
                return i
            if (arr[i] > element or
                i+1 == len(arr) or
                arr[i] > arr[i+1]):
                return None
    else:
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == element:
                return i
            if (arr[i] < element or
                i == 0 or
                arr[i] < arr[i-1]):
                return None