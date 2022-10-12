'''
Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
'''

from typing import List

def getAllPermutations(num_arr: List[int]):
    def rGetAllPermutations(remaining_arr, current_arr, permutation_list):
        if len(remaining_arr) == 0:
            permutation_list.append(current_arr.copy()) # Working with primitives; no need to deep copy.
            return

        for i, number in enumerate(remaining_arr):
            current_arr.append(number)
            rGetAllPermutations(remaining_arr[:i] + remaining_arr[i+1:], current_arr, permutation_list)
            current_arr.pop()
        return

    all_permutations = []
    rGetAllPermutations(num_arr, [], all_permutations)
    return all_permutations

print(getAllPermutations([1, 2, 3, 4]))