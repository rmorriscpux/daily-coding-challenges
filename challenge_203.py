'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
Find the minimum element in O(log N) time. You may assume the array does not contain duplicates.

For example, given [5, 7, 10, 3, 4], return 3.
'''

from typing import List

# Not using min(), obviously.
# This is similar to the first step of merge sorting.
def minElement(int_arr: List[int]):
    arr_len = len(int_arr)
    # End case.
    if arr_len == 1:
        return int_arr[0]

    # Get pivot spot in middle.
    pivot = arr_len // 2

    # Check if pivot location contains the minimum.
    if int_arr[pivot] < int_arr[pivot-1]:
        return int_arr[pivot]

    # Determine if the minimum is to the left or right of the pivot.
    if int_arr[pivot] < int_arr[0]: # Minimum is to the left of pivot. Recur with the left slice.
        return minElement(int_arr[:pivot])
    elif int_arr[pivot] > int_arr[arr_len-1]: # Minimum is to the right of pivot. Recur with the right slice.
        return minElement(int_arr[pivot+1:])
    else:# Sub-array is not rotated. Minimum is at position 0.
        return int_arr[0]
            

print(minElement([5, 7, 10, 3, 4]))