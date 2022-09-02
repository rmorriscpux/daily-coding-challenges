'''
Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0).
You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.
'''

from random import random

# Simple function that takes in a threshold between 0 and 1, selects a random number,
# and returns 0 or 1 depending on whether it's lower or higher than the threshold.
def tossBiased(coin_bias: float):
    if coin_bias < 0 or coin_bias >= 1:
        raise ValueError("coin_bias must be between 0 and 1")
    return 0 if random() <= coin_bias else 1

# Monte Carlo test of the function.
bias = random()
trials = 100000
count = [0, 0]
for i in range(trials):
    count[tossBiased(bias)] += 1
print(f'''Coin Bias: {bias}
   Trials: {trials}
 % Zeroes: {count[0] / trials * 100}%
   % Ones: {count[1] / trials * 100}%''')