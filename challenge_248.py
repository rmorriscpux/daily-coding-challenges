'''
Find the maximum of two numbers without using any if-else statements, branching, or direct comparisons.
'''

def maxNum(n1: int, n2: int) -> int:
    diff = n1 - n2
    # Python's integer memory allocation is dynamic, and bitwise shift operations perform a simulated two's complement fill.
    # k will end up being -1 if n2 is greater than n1 (i.e. diff is negative), otherwise k will be 0.
    k = diff
    while k not in [-1, 0]:
        # Number of bits to shift is arbitrary. 63 covers all signed 64-bit integers in one iteration.
        k >>= 63
    # Returns n1 if k == 0, n2 if k == -1.
    return n1 + diff * k

print(maxNum(17, 5))
print(maxNum(5, 18))