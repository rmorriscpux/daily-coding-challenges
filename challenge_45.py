'''
Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability,
implement a function rand7() that returns an integer from 1 to 7 (inclusive).
'''

import random

def rand5():
    return random.randint(1, 5)

def rand7():
        # Obtain a uniformly random draw between 1 and 25 by using rand5(). Sums one of {0, 5, 10, 15, 20} with one of {1, 2, 3, 4, 5}
    rand_draw = (rand5() - 1) * 5 + rand5()

        # To scale, redraw if we get a draw above 21.
        # Average number of loop iterations = Σ(4/25)^k for integers k from 1 to ∞, which is approximately 0.1905.
        # This means the average number of calls to rand5(), including the initial setup, is 2.3810.
    while rand_draw > 21:
        rand_draw = (rand5() - 1) * 5 + rand5()

    # Since our range is 21 integers with equivalent occurrence, and 21 is evenly divisible by 7,
    # then each modulus (0-6) occurs with uniform probability as well. Add 1 to get the range (1-7).
    return (rand_draw % 7) + 1

trials = 100000
results = {}
for i in range(1, 8):
    results[i] = 0
for i in range(0, trials):
    r = rand7()
    results[r] += 1
print(trials, "Trials:")
print(results)