'''
Given an array of integers, find the maximum XOR of any two elements.
'''

from typing import List

def getMaxXor(int_arr: List[int]) -> int:
    if len(int_arr) <= 1:
        raise IndexError("Need at least two integers to XOR")
    
    max_xor = float('-inf')
    for i in range(0, len(int_arr)-1):
        for j in range(i+1, len(int_arr)):
            max_xor = max(max_xor, i ^ j)

    return max_xor

