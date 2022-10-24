'''
Given a set of closed intervals, find the smallest set of numbers that covers all the intervals. If there are multiple smallest sets, return any of them.

For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers that covers all these intervals is {3, 6}.
'''

from typing import Tuple

def getSmallestSet(*intervals: Tuple[int, int]):
    # No parameters passed.
    if len(intervals) == 0:
        return set()

    # Get the highest start value and the lowest end value.
    highest_start, lowest_end = float('-inf'), float('inf')
    for (start, end) in intervals:
        highest_start = max(start, highest_start)
        lowest_end = min(end, lowest_end)
    
    if highest_start == lowest_end:
        # All are covered in a single value.
        return {highest_start}
    elif highest_start > lowest_end:
        # The edges overlap all intervals at least partially.
        return {lowest_end, highest_start}
    else:
        # Determine how small we can make the set. First build a dictionary mapping numbers to intervals.
        nums_in_intervals = {}
        for num in range(highest_start, lowest_end+1):
            if num not in nums_in_intervals:
                nums_in_intervals[num] = []
            for i in intervals:
                if num >= i[0] and num <= i[1]:
                    nums_in_intervals[num].append(i)
            if len(nums_in_intervals[num]) == len(intervals):
                # Case where all intervals can be covered by a single integer.
                return {num}

        # Need to find a range since not all intervals overlap with each other.
        out_range = set()
        interval_set = set(intervals)

        # Go backward from lowest_end to highest_start until all intervals are in the set. At that point we have the start value.
        intervals_to_add = set()
        for start_num in range(lowest_end, highest_start-1, -1):
            intervals_to_add.union(set(nums_in_intervals[start_num]))
            if len(intervals_to_add) == len(interval_set):
                out_range.add(start_num)
                break
        
        # Go forward from highest_start to lowest_end until all intervals are in the set. At that point we have the end value.
        intervals_to_add.clear()
        for end_num in range(highest_start, lowest_end+1):
            intervals_to_add = intervals_to_add.union(set(nums_in_intervals[end_num]))
            if len(intervals_to_add) == len(interval_set):
                out_range.add(end_num)
                break

        return out_range

print(getSmallestSet((0, 3), (2, 6), (3, 4), (6, 9)))