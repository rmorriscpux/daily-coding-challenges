'''
Let X be a set of n intervals on the real line. We say that a set of points P "stabs" X if every interval in X contains at least one point in P.
Compute the smallest set of points that stabs X.

For example, given the intervals [(1, 4), (4, 5), (7, 9), (9, 12)], you should return [4, 9].
'''

from typing import List, Tuple
from copy import deepcopy

def stabIntervals(X: List[Tuple[int, int]]):
    def rStabIntervals(remaining_X: List[Tuple[int, int]]):
        # End case: Empty remaining_X list. Return empty set.
        if not remaining_X:
            return set()

        highest_start = max(map(lambda interval: interval[0], remaining_X))
        lowest_end = min(map(lambda interval: interval[1], remaining_X))

        if lowest_end >= highest_start:
            # All remaining intervals are within the bound (highest_start, lowest_end) inclusive. Add only one number to a set.
            return {highest_start}
        else:
            # Intervals may exist between the highest start and lowest end.
            i = 0
            while i < len(remaining_X):
                # Remove all intervals stabbed by highest_start or lowest_end.
                if (highest_start >= remaining_X[i][0] and highest_start <= remaining_X[i][1]) or (lowest_end >= remaining_X[i][0] and lowest_end <= remaining_X[i][1]):
                    remaining_X.pop(i)
                else:
                    i += 1

            # Return highest start, lowest end, and the result of recursion with remaining intervals.
            return {highest_start, lowest_end}.union(rStabIntervals(remaining_X))

    assert all(map(lambda interval: interval[0] <= interval[1], X)) # Optional input check.

    return rStabIntervals(deepcopy(X))

print(stabIntervals([(1, 4), (4, 5), (7, 9), (9, 12)]))
print(stabIntervals([(0, 10), (1, 6), (4, 12)]))
print(stabIntervals([(0, 1), (2, 3), (4, 5), (6, 7)]))