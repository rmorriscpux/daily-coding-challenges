'''
You have n fair coins and you flip them all at the same time. Any that come up tails you set aside.
The ones that come up heads you flip again. How many rounds do you expect to play before only one coin remains?

Write a function that, given n, returns the number of rounds you'd expect to play until one coin remains.
'''

# n is divided by 2 on every round until 1 is reached.
# Below solutions work quicker than straight division in computing.

from ctypes import c_uint
from math import log

# Shift right logical down to 1.
def expectedRounds1(n: c_uint):
    count = 0
    while n > 1:
        n >>= 1
        count += 1
        # For estimation purposes, add an extra round if n >= 2^k + 2^(k-1)
        if n == 3: #0b11
            count += 1

    return count

# Shift a variable left up to n.
def expectedRounds2(n: c_uint):
    round_growth = 1
    count = 0
    while True:
        round_growth <<= 1
        if round_growth >= n:
            break
        count += 1
    # For estimation purposes, add an extra round if n >= 2^k + 2^(k-1)
    if round_growth - n < round_growth >> 2:
        count += 1
    
    return count

# Using log_2
def expectedRounds3(n: c_uint):
    return round(log(n, 2))

print(expectedRounds1(100))
print(expectedRounds2(100))
print(expectedRounds3(100))