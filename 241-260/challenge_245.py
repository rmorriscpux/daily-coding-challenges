'''
You are given an array of integers, where each element represents the maximum number of steps that can be jumped going forward from that element.
Write a function to return the minimum number of jumps you must take in order to get from the start to the end of the array.

For example, given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2, as the optimal solution involves jumping from 6 to 5, and then from 5 to 9
'''

from typing import List

def minJumps(int_arr: List[int]):
    if len(int_arr) <= 1:
        return 0

    steps = 0
    cur_index = 0

    while True:
        steps += 1
        if cur_index + int_arr[cur_index] >= len(int_arr)-1:
            # At this point the end can be reached.
            return steps
        elif int_arr[cur_index] == 0:
            # Impossible to complete the jumps.
            return None

        next_index = None
        next_step = 0
        # Find the max sum of a jumpable index and its value.
        for i in range(cur_index+1, cur_index+1+int_arr[cur_index]):
            if i + int_arr[i] > next_step and int_arr[i] != 0:
                next_index = i
                next_step = i + int_arr[i]
        else:
            if not next_index:
                # Impossible to complete the jumps.
                return None

        cur_index = next_index

    return

print(minJumps([6, 2, 4, 0, 5, 1, 1, 4, 2, 9]))