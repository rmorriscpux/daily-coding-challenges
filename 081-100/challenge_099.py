'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''

from typing import List

class Range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __len__(self):
        return self.end - self.start + 1

def longestConsecutiveElements(num_arr: List[int]):
    starts = {}
    ends = {}
    max_range = 0

    for n in num_arr:
        if n-1 in ends and n+1 in starts:
            new_range = Range(ends[n-1].start, starts[n+1].end)
            starts[new_range.start] = new_range
            ends[new_range.end] = new_range
            del ends[n-1]
            del starts[n+1]
        elif n-1 in ends:
            new_range = ends[n-1]
            new_range.end = n
            ends[n] = new_range
            del ends[n-1]
        elif n+1 in starts:
            new_range = starts[n+1]
            new_range.start = n
            starts[n] = new_range
            del starts[n+1]
        else:
            new_range = Range(n, n)
            starts[n] = new_range
            ends[n] = new_range
            
        
        if len(new_range) > max_range:
            max_range = len(new_range)

    return max_range

print(longestConsecutiveElements([100, 4, 200, 1, 3, 2]))