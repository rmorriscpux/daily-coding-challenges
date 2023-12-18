'''
A regular number in mathematics is defined as one which evenly divides some power of 60.
Equivalently, we can say that a regular number is one whose only prime divisors are 2, 3, and 5.

These numbers have had many applications, from helping ancient Babylonians keep time to tuning instruments according to the diatonic scale.

Given an integer N, write a program that returns, in order, the first N regular numbers.
'''

from heapq import heappush, heappop
from typing import List, Set

def getRegularNums(N: int) -> List[int]:
    def rGetRegularNums(N: int, num_heap: List[int], regular_nums: Set[int]) -> None:
        if len(regular_nums) >= N:
            return
        
        lowest_val, lowest_factors = heappop(num_heap)
        regular_nums.add(lowest_val)
        for factor in lowest_factors.keys():
            next_lowest_factors = lowest_factors.copy()
            next_lowest_factors[factor] += 1
            heappush(num_heap, (lowest_val * factor, next_lowest_factors))
        rGetRegularNums(N, num_heap, regular_nums)

    assert N > 0
    # First regular number is 60, equal to 2^2 * 3^1 * 5^1
    factor_count = {
        2 : 2,
        3 : 1,
        5 : 1
    }
    first_num = 1
    for k, v in factor_count.items():
        first_num *= k ** v

    # Populate initial numbers and factors.
    num_heap, regular_nums = list(), set()
    heappush(num_heap, (first_num, factor_count))
    rGetRegularNums(N, num_heap, regular_nums)

    return sorted(regular_nums)

if __name__ == "__main__":
    print(getRegularNums(10)) # [60, 120, 180, 240, 300, 360, 480, 540, 600, 720]