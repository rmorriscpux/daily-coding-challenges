'''
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

# Will get back to this. I have a partial solution worked out in my head, but it doesn't work on edge cases.

def largest_non_adjacent_sum(int_list):
    # Initialize the sum list.
    sum_list = [int_list[0]]

    