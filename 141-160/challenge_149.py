'''
Given a list of numbers L, implement a method sum(i, j) which returns the sum from the sublist L[i:j] (including i, excluding j).

For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]), which is 5.

You can assume that you can do some pre-processing. sum() should be optimized over the pre-processing step.
'''

from typing import List

class ListSumOptimizer:
    def __init__(self, num_arr: List[int]):
        self._num_arr = num_arr
        self._sum_arr = []
        self._calculate_sum()

    # Preprocess method. Creates a list of sums of all previous numbers prior to its index.
    def _calculate_sum(self):
        self._sum_arr = [0]
        for i, num in enumerate(self._num_arr):
            self._sum_arr.append(num + self._sum_arr[i])
        return

    # Set the num_arr to a property so that when it's modified, we can automatically recalculate _sum_arr.
    @property
    def num_arr(self):
        return self._num_arr

    @num_arr.setter
    def num_arr(self, num_arr: List[int]):
        self._num_arr = num_arr
        self._calculate_sum()
        return

    # Sum method. Due to preprocessing, we can do a single subtraction operation to get the sum from i to j instead of a loop.
    def sum(self, i: int, j: int):
        if i > j:
            raise ValueError("Start index must be less than or equal to the end index.")
        if i < 0 or j > len(self._num_arr):
            raise IndexError("Start index and/or end index out of range.")

        return self._sum_arr[j] - self._sum_arr[i]

x = ListSumOptimizer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(x.sum(3, 7)) # 22
print(x.sum(0, 10)) # 55
x.num_arr = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(x.sum(3, 7)) # 62