'''
A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

if n is even, the next number in the sequence is n / 2
if n is odd, the next number in the sequence is 3n + 1
It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.

Bonus: What input n <= 1000000 gives the longest sequence?
'''

from typing import List

def collatzSeq(n: int, steps: int=0, prev_sequence: List[int]=[]):
    assert n > 0 # Collatz only applies to positive integers.
    assert n not in prev_sequence # Any repeats prior to reaching n = 1 means there is a cycle. (Note: This doesn't happen.)
    global collatzCache

    # End case.
    if n == 1:
        return steps

    # Check if the number of steps in the sequence has already been calculated.
    if collatzCache and n in collatzCache:
        return steps + collatzCache[n]

    if n % 2 == 1:
        return collatzSeq(n * 3 + 1, steps + 1, prev_sequence + [n])
    else:
        return collatzSeq(n // 2, steps + 1, prev_sequence + [n])

# Test
collatzCache = {}

# Run Collatz Sequence starting with all integers from 1 to 1000000 inclusive.
for i in range(1, 1000001):
    collatzCache[i] = collatzSeq(i)

# Print the integer with the highest number of steps in its Collatz sequence to reach 1.
print(max(collatzCache, key=lambda k: collatzCache[k]))