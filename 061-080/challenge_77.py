'''
Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
'''

from typing import List, Tuple

# Assumption: each interval's start value is less than each interval's end value.
# This runs in O(N) time. There is also a merge-while-iterating solution that uses less space but would run in O(N^2) time.
def mergeIntervals(interval_list: List[Tuple[int, int]]):
    # Make dictionaries of counters for interval starts and ends.
    interval_starts = {}
    interval_ends = {}
    for start, end in interval_list:
        if start not in interval_starts:
            interval_starts[start] = 0
        interval_starts[start] += 1
        if end not in interval_ends:
            interval_ends[end] = 0
        interval_ends[end] += 1

    # Now create a list of integers representing where intervals occur. 
    min_start = min(list(interval_starts.keys()))
    max_end = max(list(interval_ends.keys()))
    interval_status_list = []
    interval_status = 0
    for i in range(min_start, max_end+1):
        if i in interval_starts:
            interval_status += interval_starts[i]
        if i in interval_ends:
            interval_status -= interval_ends[i]
        interval_status_list.append(interval_status)

    # Build a new list of interval tuples based on the above list.
    # The value for each index is greater than 0 if covered by an interval, not counting the end point.
    start = min_start
    end = None

    merged_list = []
    for i in range(1, len(interval_status_list)):
        if interval_status_list[i] > 0 and interval_status_list[i-1] == 0:
            start = min_start + i
        if interval_status_list[i] == 0 and interval_status_list [i-1] > 0:
            end = min_start + i
            merged_list.append((start, end))

    return merged_list

print(mergeIntervals([(1, 3), (5, 8), (4, 10), (20, 25)]))
print(mergeIntervals([(1, 3), (5, 8), (20, 27), (4, 10), (20, 25)]))