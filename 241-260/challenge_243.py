'''
Given an array of numbers N and an integer k, your task is to split N into k partitions such that the maximum sum of any partition is minimized. Return this sum.

For example, given N = [5, 1, 2, 7, 3, 4] and k = 3, you should return 8, since the optimal partition is [5, 1, 2], [7], [3, 4].
'''

from typing import List

def partitionNumbers(N: List[int], k: int) -> int:
    def rPartitionNumbers(N: List[int], k: int):
        # End case.
        if k == 1:
            return ([N], sum(N))

        min_val = float('inf')
        possible_min = (None, None)
        # Split at each position i, come back with the smallest possible sum.
        for i in range(0, len(N)):
            a1, s1 = ([N[:i]], sum(N[:i]))
            a2, s2 = rPartitionNumbers(N[i:], k-1)
            cur_min = a1 + a2, max(s1, s2)
            if cur_min[1] < min_val:
                min_val = cur_min[1]
                possible_min = cur_min

        return possible_min

    assert 0 < k <= len(N)

    return rPartitionNumbers(N, k)[1]

print(partitionNumbers([5, 1, 2, 7, 3, 4], 3))