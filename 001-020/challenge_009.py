'''
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

def largestNonAdjacentSum(int_list):
    prev_sum = 0
    sum = 0

    # Compare in a cascading fashion so that in the end adjacent numbers are not added together.
    for num in int_list:
        temp_sum = sum
        sum = max(sum, prev_sum + num)
        prev_sum = temp_sum
    return sum

print(largestNonAdjacentSum([2, 4, 6, 2, 5]))
print(largestNonAdjacentSum([5, 1, 1, 5]))