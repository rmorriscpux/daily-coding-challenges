'''
Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14
'''

from typing import List

def findGCD(int_list: List[int]):
    # The greatest common denominator is no larger than the smallest absolute value in the list.
    min_int = min(list(map(lambda num : abs(num), int_list)))

    # Check every number starting at 1 up to min_int divided by 2. Use the factor to calculate the denominator if min_int is evenly divisible by it (modulo is 0).
    for factor in range(1, min_int // 2 + 1):
        if min_int % factor == 0:
            denominator = min_int // factor
            # Check if all integers in the list are divisible by the denominator. Return the denominator if they all are.
            if all(list(map(lambda num : num % denominator == 0, int_list))):
                return denominator
    # If loop completes, the GCD is 1.
    return 1

print(findGCD([42, 56, 14]))
print(findGCD([-42, -56, 14]))
print(findGCD([42, 56, 13]))
print(findGCD([24, 15, 27, 81]))