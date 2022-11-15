'''
Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice, find the two elements that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.

Follow-up: Can you do this in linear time and constant space?
'''

from typing import List

# Method 1: Using Set. Add a number if it's not in the set, and remove it if it is.
def findSingleElements1(int_arr: List[int]):
    out_set = set()

    for num in int_arr:
        if num in out_set:
            out_set.remove(num)
        else:
            out_set.add(num)

    # Convert to list or tuple if desired. Leaving as a set here.
    return out_set

print(findSingleElements1([2, 4, 6, 8, 10, 2, 6, 10]))

# Method 2: Using bitwise XOR. This works on the axiom that for any value n, n ^ n = 0.
def findSingleElements2(int_arr: List[int]):
    # Do a XOR across all elements.
    arr_xor = 0
    for num in int_arr:
        arr_xor ^= num
    # arr_xor now equals the two single elements XOR'd. We now need to know the first bit where they differ in order to determine the elements' values.
    # This is accomplished by a bitwise AND between itself and the inverse of itself minus 1.
    first_different_bit = arr_xor & ~(arr_xor - 1)
    # We can then split the difference in the same manner as above. One element will ultimately land in s1, and the other in s2, with all others filtered out.
    s1, s2 = 0, 0
    for num in int_arr:
        if num & first_different_bit:
            s1 ^= num
        else:
            s2 ^= num

    return s1, s2

print(findSingleElements2([2, 4, 6, 8, 10, 2, 6, 10]))