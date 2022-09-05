'''
Given a function that generates perfectly random numbers between 1 and k (inclusive),
where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
'''

import random
from typing import List

def shuffleDeck(card_deck: List):
    num_cards = len(card_deck)

    for card_position in range(0, num_cards):
        # Get random swap position. Previous positions are frozen in place. The range shrinks each iteration, so that the total number of permutations is 52!.
        swap_position = random.randrange(card_position, num_cards)
        # Swap
        temp = card_deck[card_position]
        card_deck[card_position] = card_deck[swap_position]
        card_deck[swap_position] = temp

    return

suits = "♠♣♥♦"
ranks = "A23456789TJQK"

card_deck = []
for s in suits:
    for r in ranks:
        card_deck.append(r+s)

print(card_deck)
shuffleDeck(card_deck)
print(card_deck)

for s in suits:
    for r in ranks:
        assert (r+s) in card_deck