'''
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Intervals can "touch", such as [0, 1] and [1, 2], but they won't be considered overlapping.

For example, given the intervals (7, 9), (2, 4), (5, 8), return 1 as the last interval can be removed and the first two won't overlap.

The intervals are not necessarily sorted in any order.
'''

from typing import List, Tuple

def intervalsToRemove(intervals: List[Tuple[int, int]]):
    # Combine all overlap conditions into a single boolean value.
    overlapping = lambda r1, r2: (
        (r1[0] > r2[0] and r1[0] < r2[1]) or
        (r1[1] > r2[0] and r1[1] < r2[1]) or
        (r2[0] > r1[0] and r2[0] < r1[1]) or
        (r2[1] > r1[0] and r2[1] < r1[1]) or
        (r1[0] == r2[0] and r1[1] == r2[1])
    )

    def rIntervalsToRemove(intervals_remaining, removed):
        total_removed = None
        for i, cur_interval in enumerate(intervals_remaining):
            for j, comp_interval in enumerate(intervals_remaining):
                # Do not self-compare intervals.
                if i == j:
                    continue

                # When an overlap is found, recur with cur_interval removed from the list of intervals.
                # Looking to obtain the overall minimum case here.
                if (overlapping(cur_interval, comp_interval)):
                    if total_removed:
                        total_removed = min(total_removed, rIntervalsToRemove(intervals_remaining[:i] + intervals_remaining[i+1:], removed + 1))
                    else:
                        total_removed = rIntervalsToRemove(intervals_remaining[:i] + intervals_remaining[i+1:], removed + 1)
                    break

        # Return the 'removed' value if the function doesn't recur.
        return total_removed if total_removed else removed

    # Check that intervals are valid.
    for interval in intervals:
        assert interval[0] < interval[1]

    return rIntervalsToRemove(intervals, 0)

print(intervalsToRemove([(7, 9), (2, 4), (5, 8)]))