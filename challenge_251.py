'''
Given an array of a million integers between zero and a billion, out of order,
how can you efficiently sort it? Assume that you cannot store an array of a billion elements in memory.
'''

from typing import List

# 1: Merge Sort -> O(N*log(N))
def mergeSort(int_list: List[int]) -> List[int]:
    def rMergeSort(list_segment: List[int]):
        if len(list_segment) == 1:
            return list_segment
        
        pivot = len(list_segment) // 2
        left_segment = rMergeSort(list_segment[:pivot])
        right_segment = rMergeSort(list_segment[pivot:])

        sorted_list = []
        while left_segment and right_segment:
            if left_segment[0] < right_segment[0]:
                sorted_list.append(left_segment.pop(0))
            else:
                sorted_list.append(right_segment.pop(0))

        if left_segment:
            sorted_list.extend(left_segment)
        if right_segment:
            sorted_list.extend(right_segment)

        return sorted_list
    
    return rMergeSort(int_list)

#2: Convert to Heap -> O(N*log(N))