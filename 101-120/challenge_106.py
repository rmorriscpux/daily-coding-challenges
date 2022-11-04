'''
Given an integer list where each number represents the number of hops you can make, determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns true while [1, 1, 0, 1] returns false.
'''

from typing import List

def reachLastIndex(num_arr: List[int]):
    traversed = set()
    current_index = 0
    arr_length = len(num_arr)

    while current_index != arr_length - 1:
        if current_index in traversed:
            return False

        traversed.add(current_index)
        current_index += num_arr[current_index]

        if current_index < 0 or current_index >= arr_length:
            return False

    return True

print(reachLastIndex([2, 0, 1, 0]))
print(reachLastIndex([1, 1, 0, 1]))
print(reachLastIndex([-1, 1, 0, 1]))
print(reachLastIndex([2, 2, -1, 1]))
