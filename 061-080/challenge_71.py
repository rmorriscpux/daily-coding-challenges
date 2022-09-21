'''
Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability,
implement a function rand5() that returns an integer from 1 to 5 (inclusive).
'''

import random

def rand7():
    return random.randint(1, 7)

# Version 1: Fewer average calls to rand7(), but with a higher volatility.
def rand5_1():
    # Obtain a uniformly random draw between 1 and 7 by using rand7()
    rand_num = rand7()

        # To scale, redraw if we get a draw above 5.
        # Average number of loop iterations = Σ(2/7)^k for integers k from 1 to ∞, which is approximately 0.6665.
        # This means the average number of calls to rand7(), including the initial setup, is 1.6665.
    while rand_num > 5:
        rand_num = rand7()

    return rand_num

# Version 2: More average calls to rand7(), but with a lower volatility.
def rand5_2():
    # Obtain a uniformly random draw between 1 and 49 by using rand7(). Sums one of {0, 7, 14, 21, 28, 35, 42} with one of {1, 2, 3, 4, 5, 6, 7}
    rand_num = (rand7() - 1) * 7 + rand7()

        # To scale, redraw if we get a draw above 45.
        # Average number of loop iterations = Σ(4/49)^k for integers k from 1 to ∞, which is approximately 0.0889.
        # This means the average number of calls to rand7(), including the initial setup, is 2.1778.
    while rand_num > 45:
        rand_num = (rand7() - 1) * 7 + rand7()

    return (rand_num % 5) + 1

# Select function to use and number of trials to run in test here.
rand5 = rand5_1
trials = 100000

results = {}
for i in range(1, 6):
    results[i] = 0
for i in range(0, trials):
    r = rand5()
    results[r] += 1
print(trials, "Trials:")
print(results)