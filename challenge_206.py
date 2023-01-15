'''
A permutation can be specified by an array P, where P[i] represents the location of the element at i in the permutation.
For example, [2, 1, 0] represents the permutation where elements at the index 0 and 2 are swapped.

Given an array and a permutation, apply the permutation to the array. For example,
given the array ["a", "b", "c"] and the permutation [2, 1, 0], return ["c", "b", "a"].
'''

from typing import List

def validPermutation(P: List[int]):
    return all(map(lambda num: num >= 0 and num < len(P), P)) and len(P) == len(set(P))

def applyPermutation(arr: list, P: List[int]):
    # assert validPermutation(P)
    return [arr[P[i]] for i in range(0, len(P))]

def applyPermutationInPlace(arr: list, P: List[int]):
    pass

print(applyPermutation(['a', 'b', 'c'], [2, 1, 0]))
print(applyPermutation(['a', 'b', 'c', 'd'], [2, 1, 0, 3]))