'''
Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true,
since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum.
'''

from typing import List

def splitSum(num_set: List[int]):
    total = sum(num_set)
    # Cannot be split into equal sums if the total sum is odd.
    if total % 2 == 1:
        return False

    def rSplitSum(sum_list, remaining_list, target_sum):
        # Goal - Reached the target sum of total / 2
        if sum(sum_list) == target_sum:
            return True

        # Go back if remaining list is empty or we have a sum larger than the target.
        if (len(remaining_list) == 0 or
            sum(sum_list) > target_sum):
            return False

        # Recur-and-backtrack routine to find a match for the target sum.
        for i in range(0, len(remaining_list)):
            sum_list.append(remaining_list[i])
            if rSplitSum(sum_list, remaining_list[i+1:], target_sum):
                return True
            sum_list.pop()

        return False

    # Return result with the initial setup.
    return rSplitSum([], num_set, total // 2)

print(splitSum([15, 5, 20, 10, 35, 15, 10]))
print(splitSum([15, 5, 20, 10, 35]))
print(splitSum([2, 4, 8, 16, 32]))