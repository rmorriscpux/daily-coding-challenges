'''
Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4].
'''

from typing import List

def contiguousSum(int_arr: List[int], k: int):
    start = 0
    end = 0
    sum = 0

    while end <= len(int_arr):
        if sum == k:
            return int_arr[start:end]
        elif sum > k:
            if k < 0:
                if end < len(int_arr):
                    sum += int_arr[end]
                end += 1
            else:
                sum -= int_arr[start]
                start += 1
                if start > end:
                    end = start
        else:
            if k < 0:
                sum -= int_arr[start]
                start += 1
                if start > end:
                    end = start
            else:
                if end < len(int_arr):
                    sum += int_arr[end]
                end += 1

    return None

print(contiguousSum([1, 2, 3, 4, 5], 9))