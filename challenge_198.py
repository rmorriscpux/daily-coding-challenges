'''
Given a set of distinct positive integers, find the largest subset such that every pair of elements in the subset (i, j) satisfies either i % j = 0 or j % i = 0.

For example, given the set [3, 5, 10, 20, 21], you should return [5, 10, 20]. Given [1, 3, 6, 24], return [1, 3, 6, 24].
'''

from typing import List

def largestAllDivisible(int_set: set):
    def rLargestAllDivisible(int_list: List[int], index: int, last_factor: int, cur_set: set):
        # End case.
        if index == len(int_list):
            return cur_set

        # Result 1: Recursion ignoring the integer at the current index.
        result1 = rLargestAllDivisible(int_list, index+1, last_factor, cur_set)
        # Result 2: Recursion with the integer at the current index included in the set if it's divisible by the last factor. Otherwise, empty set.
        result2 = set()
        if int_list[index] % last_factor == 0:
            result2 = rLargestAllDivisible(int_list, index+1, int_list[index], cur_set.union({int_list[index]}))
        
        # Return largest result.
        return result1 if len(result1) > len(result2) else result2

    # Input check
    assert all(map(lambda n: isinstance(n, int) and n > 0, int_set))

    return rLargestAllDivisible(sorted(list(int_set)), 0, 1, set())

print(largestAllDivisible({3, 5, 10, 20, 21}))
print(largestAllDivisible({1, 3, 6, 24}))