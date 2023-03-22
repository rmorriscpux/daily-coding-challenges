'''
MegaCorp wants to give bonuses to its employees based on how many lines of codes they have written.
They would like to give the smallest positive amount to each worker consistent with the constraint that
if a developer has written more lines of code than their neighbor, they should receive more money.

Given an array representing a line of seats of employees at MegaCorp, determine how much each one should get paid.

For example, given [10, 40, 200, 1000, 60, 30], you should return [1, 2, 3, 4, 2, 1].
'''

from typing import List

def getBonuses(lines_per_dev: List[int]):
    # Return empty list on empty input.
    if len(lines_per_dev) == 0:
        return []
    # Return single-item minimum list on single-item list.
    if len(lines_per_dev) == 1:
        return [1]
    # Determine the index with the max value.
    max_index = 0
    for i in range(1, len(lines_per_dev)):
        if lines_per_dev[i] > lines_per_dev[max_index]:
            max_index = i
    # Get bonus arrays for the left and right side of the max.
    left = getBonuses(lines_per_dev[:max_index])
    right = getBonuses(lines_per_dev[max_index+1:])
    # Combine arrays. For the current max, compare neighbors' bonus and add 1.
    return left + [max(left[-1:] + right[:1]) + 1] + right

print(getBonuses([10, 40, 200, 1000, 60, 30]))
print(getBonuses([1000, 40, 200, 1000, 60, 30]))