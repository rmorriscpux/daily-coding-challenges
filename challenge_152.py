'''
You are given n numbers as well as n probabilities that sum up to 1. Write a function to generate one of the numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2],
your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.
'''

from random import random
from typing import List

class WeightedRandom:
    def __init__(self, numbers: List[int], probabilities: List[float]):
        assert len(numbers) == len(probabilities)
        assert len(numbers) > 0
        assert sum(probabilities) == 1

        self._numbers = numbers
        # Preprocess probabilities to generate randoms faster.
        self._thresholds = [0]
        for i, p in enumerate(probabilities):
            self._thresholds.append(self._thresholds[i] + p)

    def getWeightedRandom(self):
        # Binary search for the place the random value falls in between. Runs in O(log(N)) time, whereas simple list traversal runs in O(N) time.
        def binaryPlace(rand_val, begin, end):
            middle = (begin + end) // 2
            if rand_val < self._thresholds[middle]:
                return binaryPlace(rand_val, begin, middle)
            elif rand_val >= self._thresholds[middle+1]:
                return binaryPlace(rand_val, middle+1, end)
            else:
                return middle

        return self._numbers[binaryPlace(random(), 0, len(self._thresholds) - 1)]

TRIALS = 1000000

r = WeightedRandom([1, 2, 3, 4], [0.1, 0.5, 0.2, 0.2])

results = {}

for i in range(TRIALS):
    rand_num = r.getWeightedRandom()
    if rand_num not in results:
        results[rand_num] = 0
    results[rand_num] += 1

# Sort results by value and print.
for rand_result, total in sorted(results.items(), key=lambda i: i[0]):
    print(f"{rand_result}: {format(total/TRIALS*100, '.4f')}%")