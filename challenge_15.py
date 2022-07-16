'''
Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
'''

import random

def pick_from_stream(stream):
    # Initialize selection
    selection = None

    # We will be assigning a random value to each element and selecting the element that receives the lowest value.
    min_val = 1.0
    for element in stream:
        rand_val = random.random()

        # If lower than the stored lowest value, make the current element the selection.
        if rand_val < min_val:
            min_val = rand_val
            selection = element

    return selection