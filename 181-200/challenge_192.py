'''
You are given an array of nonnegative integers. Let's say you start at the beginning of the array and are trying to advance to the end.
You can advance at most, the number of steps that you're currently on. Determine whether you can get to the end of the array.

For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices 0 -> 1 -> 3 -> 5, so return true.

Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false
'''

from typing import List

def endReachable(int_list: List[int]):
    def rEndReachable(int_list, position):
        # At the final position.
        if position == len(int_list) - 1:
            return True
        elif position >= len(int_list):
            return False

        # Move forward until we reach the final position or a dead end.
        for step in range(1, int_list[position]+1):
            if rEndReachable(int_list, position+step):
                return True

        return False

    # Check that the input list is not empty and that all integers in the list are nonnegative.
    if len(int_list) == 0:
        return False
    assert all(map(lambda k: k >= 0, int_list))

    return rEndReachable(int_list, 0)

print(endReachable([1, 3, 1, 2, 0, 1]))
print(endReachable([1, 2, 1, 0, 0]))