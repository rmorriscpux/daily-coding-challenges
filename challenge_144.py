'''
Given an array of numbers and an index i, return the index of the nearest larger number of the number at index i, where distance is measured in array indices.

For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

If two distances to larger numbers are the equal, then return any one of them. If the array at i doesn't have a nearest larger integer, then return null.

Follow-up: If you can preprocess the array, can you do this in constant time?
'''

from typing import List

def nearestLargerNumberIndex(arr: List[int], i: int):
    if i < 0 or i >= len(arr):
        raise IndexError("Index i out of range.")

    dist = 1
    while i - dist >= 0 or i + dist < len(arr):
        if i - dist >= 0 and arr[i - dist] > arr[i]:
            return i - dist
        if i + dist < len(arr) and arr[i + dist] > arr[i]:
            return i + dist
        dist += 1

    return None

print(nearestLargerNumberIndex([4, 1, 3, 5, 6], 0))

print(nearestLargerNumberIndex([6, 0, 7, 4, 4, 1, 3, 5, 6], 4))

# Why preprocess the array? Imagine you need to call the main function a lot. With the preprocessed array, this saves time.
# Effectively, it's a map of every next highest value's index to that index.
def numArrayPreproc(arr: List[int]):
    arr_length = len(arr)
    preproc_arr = [None for i in range(0, arr_length)]
    for index, val in enumerate(arr):
        # Find the closest higher value if it exists.
        dist = 1
        while index - dist >= 0 or index + dist < arr_length:
            if index - dist >= 0 and arr[index - dist] > val:
                preproc_arr[index] = index - dist
                break
            if index + dist < arr_length and arr[index + dist] > val:
                preproc_arr[index] = index + dist
                break
            dist += 1

    return preproc_arr

def nearestLargerNumberIndexPreproc(preproc_arr: list, i: int):
    return preproc_arr[i]