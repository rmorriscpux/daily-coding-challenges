'''
Given an array of positive integers, divide the array into two subsets such that the difference between the sum of the subsets is as small as possible.

For example, given [5, 10, 15, 20, 25], return the sets {10, 25} and {5, 15, 20}, which has a difference of 5, which is the smallest possible difference.
'''

from typing import List

def divideIntegers(int_arr: List[int]):
    def minimizeDiff(arr1, arr1_sum, arr2, arr2_sum, diff):
        min_diff = diff
        next_args = None

        for i, num in enumerate(arr1):
            new_arr1_sum = arr1_sum - num
            new_arr2_sum = arr2_sum + num
            new_diff = abs(new_arr1_sum - new_arr2_sum)
            if new_diff < min_diff:
                min_diff = new_diff
                next_args = [arr1[:i] + arr1[i+1:], new_arr1_sum, arr2 + [num], new_arr2_sum]

        if not next_args:
            return (arr1, arr2)

        return minimizeDiff(next_args[0], next_args[1], next_args[2], next_args[3], min_diff)

    int_arr_sum = sum(int_arr)
    return minimizeDiff(int_arr, int_arr_sum, [], 0, int_arr_sum)

    
    int_sum = sum(int_arr)

print(divideIntegers([5, 10, 15, 20, 25]))