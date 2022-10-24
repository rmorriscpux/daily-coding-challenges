'''
Given a set of closed intervals, find the smallest set of numbers that covers all the intervals. If there are multiple smallest sets, return any of them.

For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers that covers all these intervals is {3, 6}.
'''

from typing import Tuple

def getSmallestSet(*intervals: Tuple[int, int]):
    if len(intervals) == 0:
        return None

    highest_start, lowest_end = float('-inf'), float('inf')
    for (start, end) in intervals:
        highest_start = max(start, highest_start)
        lowest_end = min(end, lowest_end)
    
    if highest_start == lowest_end:
        return {highest_start}
    elif highest_start > lowest_end:
        return {lowest_end, highest_start}
    else:
        nums_in_intervals = {}
        for num in range(highest_start, lowest_end+1):
            if num not in nums_in_intervals:
                nums_in_intervals[num] = []
            for i in intervals:
                if num >= i[0] and num <= i[1]:
                    nums_in_intervals[num].append(i)
            if len(nums_in_intervals[num]) == len(intervals):
                return {num}

        out_range = set()

        intervals_to_add = set()
        for start_num in range(lowest_end, highest_start-1, -1):
            intervals_to_add.union(set(nums_in_intervals[start_num]))
            if len(intervals_to_add) == len(intervals):
                out_range.add(start_num)
                break
        
        intervals_to_add = set()
        for end_num in range(highest_start, lowest_end+1):
            intervals_to_add.union(set(nums_in_intervals[end_num]))
            if len(intervals_to_add) == len(intervals):
                out_range.add(end_num)
                break

        return out_range

print(getSmallestSet((0, 3), (2, 6), (3, 4), (6, 9)))