'''
Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability,
implement a function rand7() that returns an integer from 1 to 7 (inclusive).
'''

import random

def rand5():
    return random.randint(1, 5)

def rand7():
    rand_draw = 25
    while rand_draw > 21:
        # Obtain a uniformly random draw between 1 and 25 by using rand5(). Sums one of {0, 5, 10, 15, 20} with one of {1, 2, 3, 4, 5}
        # To scale, redraw if we get a draw above 21.
        rand_draw = (rand5() - 1) * 5 + rand5()
    # Since our range is 21 integers with equivalent occurrence, and 21 is evenly divisible by 7,
    # then each modulus (0-6) occurs with uniform probability as well. Add 1 to get the range (1-7).
    return (rand_draw % 7) + 1

results = {}
for i in range(1, 8):
    results[i] = 0
    trials = 100000
for i in range(0, trials):
    r = rand7()
    results[r] += 1
print(trials, "Trials:")
print(results)