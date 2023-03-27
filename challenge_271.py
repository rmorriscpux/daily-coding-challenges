'''
Given a sorted list of integers of length N, determine if an element x is in the list without performing any multiplication, division, or bit-shift operations.

Do this in O(log N) time.
'''

from random import randint
from typing import List

# In place of a standard binary search which would involve using division, select an index in the range at random as the pivot on each iteration.
# On average, this will work in O(log N) time, the same as a binary search, just with higher volatility.
# int_list is assumed to be pre-sorted.
def hasElement(x: int, int_list: List[int]) -> bool:
    # Initialize
    lo, hi = 0, len(int_list)-1

    while lo <= hi:
        selection = randint(lo, hi)
        # Move a boundary based on the selected index's value if it is not x. Return True if the selected index's value is x.
        if int_list[selection] < x:
            lo = selection + 1
        elif int_list[selection] > x:
            hi = selection - 1
        else: # int_list[selection] == x
            return True
    # x not found.
    return False
        
int_list = list(range(2, 22, 2))

print(hasElement(10, int_list))
print(hasElement(11, int_list))
print(hasElement(2, int_list))
print(hasElement(20, int_list))