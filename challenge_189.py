'''
Given an array of elements, return the length of the longest subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].
'''

def maxDistinctElements(num_arr: list):
    if (len(num_arr) == 0):
        return 0
        
    start = 0
    element_last_seen = {num_arr[0]: 0}
    max_size = 0

    for end in range(1, len(num_arr)):
        if num_arr[end] in element_last_seen and element_last_seen[num_arr[end]] >= start:
            start = element_last_seen[num_arr[end]] + 1
            max_size = max(max_size, end - start + 1)
        element_last_seen[num_arr[end]] = end

    max_size = max(max_size, end - start + 1)

    return max_size

print(maxDistinctElements([5, 1, 3, 5, 2, 3, 4, 1]))