'''
You are given a starting state start, a list of transition probabilities for a Markov chain, and a number of steps num_steps.
Run the Markov chain starting from start for num_steps and compute the number of times we visited each state.

For example, given the starting state a, number of steps 5000, and the following transition probabilities:

[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]

One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656, 'c': 332 }.
'''

# A Markov chain is a statistical map of transitions from one state to another in a state machine.
# https://en.wikipedia.org/wiki/Markov_chain

from typing import List, Tuple
from random import random
import bisect

def transitions(probabilities: List[Tuple[str, str, float]], start_state: str, num_steps: int):
    # Sort the order of probabilities just in case.
    probabilities.sort(key=lambda p: (p[0], p[1]))
    # Build transitions matrix: A dictionary of lists of values increasing to 1.0 representing ranges for the random() value to compare against.
    prev_state = ""
    prob_sum = 0
    transitions_matrix = {}
    for p in probabilities:
        if p[0] != prev_state:
            prob_sum = 0
        if p[0] not in transitions_matrix:
            transitions_matrix[p[0]] = []
        if p[1] not in transitions_matrix:
            transitions_matrix[p[1]] = []
        transitions_matrix[p[0]].append(p[2] + prob_sum)
        prob_sum += p[2]
        prev_state = p[0]
    # print(transitions_matrix)
    # Setup
    counter = {}
    states = []
    for state_key in transitions_matrix.keys():
        counter[state_key] = 0
        states.append(state_key)
    # Run Trials
    cur_state = start_state
    for i in range(0, num_steps):
        rand_val = random()
        next_state_pos = bisect.bisect_left(transitions_matrix[cur_state], rand_val)
        cur_state = states[next_state_pos]
        counter[cur_state] += 1

    print(counter)

    return

markov_chain = [
    ('a', 'a', 0.9),
    ('a', 'b', 0.075),
    ('a', 'c', 0.025),
    ('b', 'a', 0.15),
    ('b', 'b', 0.8),
    ('b', 'c', 0.05),
    ('c', 'a', 0.25),
    ('c', 'b', 0.25),
    ('c', 'c', 0.5)
]
transitions(markov_chain, 'a', 5000)
transitions(markov_chain, 'a', 1000000)