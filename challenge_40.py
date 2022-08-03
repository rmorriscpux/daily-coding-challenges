'''
Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
'''

from typing import List

def nonDuplicateInteger(array : List[int]):
    # Using the fact that set values must be unique to get a difference between the sum of all values in the list and simply tripling each unique integer.
    # This difference will be the unique value multiplied by (3-1), i.e. 2.
    arr_sum = 0
    triple_sum = 0
    unique_integers = set()
    for integer in array:
        set_length = len(unique_integers)
        arr_sum += integer
        unique_integers.add(integer)
        # Add the integer times 3 if the integer was not previously in the unique_integers set.
        # Doing this within the loop instead of having a new loop keeps O(N) time complexity.
        if len(unique_integers) > set_length: 
            triple_sum += integer * 3
    
    return (triple_sum - arr_sum) // 2

print(nonDuplicateInteger([6, 1, 3, 3, 3, 6, 6]))
print(nonDuplicateInteger([13, 19, 13, 13]))
print(nonDuplicateInteger([6, -5, 3, 3, 3, 6, 6]))