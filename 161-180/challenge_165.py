'''
Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

    There is 1 smaller element to the right of 3
    There is 1 smaller element to the right of 4
    There are 2 smaller elements to the right of 9
    There is 1 smaller element to the right of 6
    There are no smaller elements to the right of 1
'''

from typing import List

def getSmallerToRight(int_arr: List[int]):
    sorted_arr = []
    smaller_to_right = []

    for i in range(len(int_arr) - 1, -1, -1):
        for smaller_count, num in enumerate(sorted_arr):
            if num >= int_arr[i]:
                smaller_to_right.insert(0, smaller_count)
                sorted_arr.insert(smaller_count, int_arr[i])
                break
        else:
            smaller_to_right.insert(0, len(sorted_arr))
            sorted_arr.append(int_arr[i])

    return smaller_to_right

print(getSmallerToRight([3, 4, 9, 6, 1]))