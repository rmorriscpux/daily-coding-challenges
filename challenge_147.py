'''
Given a list, sort it using this method: reverse(lst, i, j), which sorts lst from i to j.
'''

from typing import List
import copy

def reverse(lst: List[int], i: int, j: int):
    return list(reversed(lst[i:j+1]))

def sortWithReverse(lst: List[int]):
    # Segment list
    start, end = None, None
    last_end = -1

    sorted_segments = []
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            if not start:
                segment = lst[last_end+1:i-1]
                if segment:
                    sorted_segments.append(segment)
                start = i-1
        elif start:
            end = i-1
            if end > start:
                sorted_segments.append(reverse(lst, start, end))
                last_end = end
                start, end = None, None

    if start:
        end = len(lst) - 1
        if end > start:
            sorted_segments.append(reverse(lst, start, end))
    else:
        segment = lst[last_end+1:]
        if segment:
            sorted_segments.append(segment)

    sorted_list = []
    merged_list = []
    for segment in sorted_segments:
        merged_list.clear()
        i1, i2 = 0, 0
        while i1 < len(sorted_list) and i2 < len(segment):
            if sorted_list[i1] < segment[i2]:
                merged_list.append(sorted_list[i1])
                i1 += 1
            else:
                merged_list.append(segment[i2])
                i2 += 1

        if i1 < len(sorted_list):
            merged_list.extend(sorted_list[i1:])

        if i2 < len(segment):
            merged_list.extend(segment[i2:])

        sorted_list = copy.deepcopy(merged_list)

    return sorted_list

print(sortWithReverse([0, 6, 4, 2, 5, 3, 1, 8, 7, 10, 9]))