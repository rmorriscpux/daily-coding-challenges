'''
Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).
'''

from random import randrange
from typing import List

def randExcluding(n: int, l: List[int]):
    if n <= 0:
        raise ValueError("n must be positive.")
    # Good idea to check if all the integers in the range are in the exclusion list. If they are, the function would potentially run forever.
    # Unfortunately, this can get super long for large n.
    for i in range(0, n):
        if i not in l:
            break
    else:
        raise ValueError("No valid integers in range.")

    # Expected number of draws: ∑(len(l)/n)^k for k = 0 to ∞, assuming all integers in l are between 0 and n.
    rand_value = randrange(0, n)
    while rand_value in l:
        rand_value = randrange(0, n)
    return rand_value

# Object Oriented Solution, sacrificing space for accelerated time, reusability.
class ExclusionaryRandom:
    def __init__(self, n: int, l: List[int]):
        if n <= 0:
            raise ValueError("n must be positive.")
        self._max = 0
        self._values = []
        self.setParameters(n, l)

    def setParameters(self, n: int=-1, l: List[int]=[]):
        if n > 0:
            self._max = n

        self._values = []
        for i in range(0, self._max):
            if i not in l:
                self._values.append(i)

        return self

    def getRandomInt(self):
        return self._values[randrange(0, len(self._values))]