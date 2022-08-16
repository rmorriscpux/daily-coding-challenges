'''
Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability,
implement a function rand7() that returns an integer from 1 to 7 (inclusive).
'''

import random

def rand5():
    return random.randint(1, 5)

def rand7():
    return ((rand5() + rand5() + rand5() + rand5() + rand5() + rand5() + rand5() - 1) % 7) + 1

results = {}
for i in range(1, 8):
    results[i] = 0
    trials = 100000
for i in range(0, trials):
    r = rand7()
    results[r] += 1
print(trials, "Trials:")
print(results)