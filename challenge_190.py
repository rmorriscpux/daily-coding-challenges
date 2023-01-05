'''
Given a circular array, compute its maximum subarray sum in O(n) time. A subarray can be empty, and in this case the sum is 0.

For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8 where the 8 is obtained from wrapping around.

Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.
'''

from typing import List

def maxSubArraySum(int_list: List[int]):
    if len(int_list) == 0:
        return 0

    sum_items = []
    cur_sum = 0
    max_sum = 0

    for k in int_list + int_list:
        while len(sum_items) >= len(int_list) or (len(sum_items) > 0 and sum_items[0] < 1):
            cur_sum -= sum_items[0]
            sum_items.pop(0)
            if cur_sum > max_sum:
                max_sum = cur_sum

        sum_items.append(k)
        cur_sum += k

        if cur_sum > max_sum:
            max_sum = cur_sum

    return max_sum

print(maxSubArraySum([8, -1, 3, 4]))
print(maxSubArraySum([-4, 5, 1, 0]))
