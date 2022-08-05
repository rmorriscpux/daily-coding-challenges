'''
Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
'''

from typing import List
import copy

def sumSet(S : List[int], k : int):
    # Recursive subroutine that incorporates backtracking.
    def rSubSet(current_sum, sub_list, rem_list, k):
        # Terminator Condition 1: current_sum equals k, so the sub_list is a valid subset.
        if current_sum == k:
            return sub_list
        # Terminator Condition 2: current_sum is greater than k, or there are no more integers in the list to sum. Invalid so return None.
        elif current_sum > k or not rem_list:
            return None
        # Add to the sub_list and go through the remaining. Backtrack if necessary.
        else:
            for i, num in enumerate(rem_list):
                sub_list.append(num)
                result = rSubSet(current_sum + num, sub_list, rem_list[i+1:], k)
                if result:
                    return result
                sub_list.pop()
        return None

    # Copy and sort input list.
    sort_S = copy.deepcopy(S)
    sort_S.sort(reverse=True)

    # Remove any integers greater than k.
    for i, num in enumerate(sort_S):
        if num <= k:
            sort_S = sort_S[i:]
            break
    else:
        # All numbers in the list are greater than k, therefore no subset that sums to k exists.
        return None

    return rSubSet(0, [], sort_S, k)

print(sumSet([12, 1, 61, 5, 9, 2], 24))
print(sumSet([12, 1, 61, 5, 9, 2], 25))