'''
Let X be a set of n intervals on the real line. We say that a set of points P "stabs" X if every interval in X contains at least one point in P.
Compute the smallest set of points that stabs X.

For example, given the intervals [(1, 4), (4, 5), (7, 9), (9, 12)], you should return [4, 9].
'''

from typing import List, Tuple
from copy import deepcopy

def stabIntervals(X: List[Tuple[int, int]]):
    def rStabIntervals(remaining_X: List[Tuple[int, int]], P: set):
        # End case: Empty remaining_X list. Return current set.
        if not remaining_X:
            return P

        highest_start = max(map(lambda interval: interval[0], remaining_X))
        lowest_end = min(map(lambda interval: interval[1], remaining_X))

        if lowest_end >= highest_start:
            # All intervals are within the bound (highest_start, lowest_end) inclusive. Add only one number to a set.
            for i in range(highest_start, lowest_end+1):
                for interval in remaining_X:
                    if i < interval[0] or i > interval[1]:
                        # i is not in an interval in remaining_X.
                        break
                else: # Found a value i within all intervals. Add that to the input set and return.
                    return P.union({i})
            # Error case. Shouldn't get here.
            raise ValueError(f"Stab value not found in interval set {remaining_X}.")
        else:
            # Intervals may exist between the highest start and lowest end.
            new_X = deepcopy(remaining_X)
            i = 0
            while i < len(new_X):
                # Remove all intervals stabbed by highest_start or lowest_end.
                if (highest_start >= new_X[i][0] and highest_start <= new_X[i][1]) or (lowest_end >= new_X[i][0] and lowest_end <= new_X[i][1]):
                    new_X.pop(i)
                else:
                    i += 1

            # Recur adding highest_start and lowest_end to P.
            return rStabIntervals(new_X, P.union({highest_start, lowest_end}))

    assert all(map(lambda interval: interval[0] <= interval[1], X))

    return rStabIntervals(X, set())

print(stabIntervals([(1, 4), (4, 5), (7, 9), (9, 12)]))
print(stabIntervals([(0, 10), (1, 6), (4, 12)]))
print(stabIntervals([(0, 1), (2, 3), (4, 5), (6, 7)]))