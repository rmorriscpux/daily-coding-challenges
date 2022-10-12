'''
Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
'''

from typing import List

def longestIncSubseq(num_arr: List[int]):
    def rLongestIncSubseq(num_arr, start_index, count_per_index):
        if start_index == len(num_arr):
            return 0

        max_count = 1 # Self
        # Effectively working backwards. If we've already calculated max_count for the index, use that value here.
        # Otherwise calculate it then come back and compare.
        for i in range(start_index+1, len(num_arr)):
            if num_arr[i] > num_arr[start_index]:
                if count_per_index[i] > 0:
                    count = count_per_index[i]
                else:
                    count = rLongestIncSubseq(num_arr, i, count_per_index) + 1
                    count_per_index[i] = count

                if count > max_count:
                    max_count = count

        return max_count

    count_per_index = [0 for i in range(0, len(num_arr))]
    return rLongestIncSubseq(num_arr, 0, count_per_index)

print(longestIncSubseq([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))