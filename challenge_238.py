'''
Blackjack is a two player card game whose rules are as follows:

The player and then the dealer are each given two cards.
The player can then "hit", or ask for arbitrarily many additional cards, so long as their total does not exceed 21.
The dealer must then hit if their total is 16 or lower, otherwise pass.
Finally, the two compare totals, and the one with the greatest sum not exceeding 21 is the winner.
For this problem, cards values are counted as follows: each card between 2 and 10 counts as their face value, face cards count as 10, and aces count as 1.

Given perfect knowledge of the sequence of cards in the deck, implement a blackjack solver that maximizes the player's score (that is, wins minus losses).
'''

# Blackjack Rules: https://en.wikipedia.org/wiki/Blackjack
# Notes:
# - In Blackjack, an ace counts as 11 if the hand total would not exceed 21. For this exercise, aces only ever count as 1.
# - Casinos typically play Blackjack using a shoe with six 52-card decks, drawing until close to the end. This uses one deck, shuffled every game, .
# - No split, double-down, or insurance plays are used here.
# - If ever motivated, I might do a casino-style Blackjack strategizer.

from enum import Enum
from random import shuffle
from typing import List

# Simplified deck that does not include suits as they are meaningless in Blackjack.
RANKS = {
    'A' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    'T' : 10,
    'J' : 10,
    'Q' : 10,
    'K' : 10
}

# Game Outcomes Enumeration
class GameOutcomes(Enum):
    WIN = 0
    LOSE = 1
    PUSH = 2

class Hand:
    def __init__(self):
        self.cards = []

    @property
    def total(self):
        values = map(lambda c: RANKS[c], self.cards)
        return sum(values)

    def addCard(self, card_deck: List[str]):
        self.cards.append(card_deck.pop(0))
        return self

def buildDeck():
    deck = []
    for k in RANKS.keys():
        deck.extend([k] * 4)
    shuffle(deck)
    return deck

def playRound():
    deck = buildDeck()
    player = Hand()
    dealer = Hand()

    player.addCard(deck)
    dealer.addCard(deck)
    player.addCard(deck)
    dealer.addCard(deck)

    while player.total < 22:
        # Determine dealer action if the player stands now.
        theoretical_dealer_total = dealer.total
        i = 0
        while theoretical_dealer_total < 17: # Dealer hits until hand total is 17 or higher.
            theoretical_dealer_total += RANKS[deck[i]]
            i += 1
        if theoretical_dealer_total > 21: 
            # Dealer bust if player stands now.
            return GameOutcomes.WIN
        elif theoretical_dealer_total < player.total: 
            # Player beats dealer if dealer stands now.
            return GameOutcomes.WIN
        elif (theoretical_dealer_total == player.total) and (player.total + RANKS[deck[0]] > 22): 
            # At this stage, a push is the best outcome for the player.
            return GameOutcomes.PUSH
        # No chance of win or push at this stage. Draw a card.
        player.addCard(deck)
    # Player bust.
    return GameOutcomes.LOSE

TRIALS = 1000000

results = [0, 0, 0]
for i in range(0, TRIALS):
    game_outcome = playRound()
    results[game_outcome.value] += 1

print("RESULTS")
print(f"Number of Trials: {TRIALS}")
print("====================")
print(f" WIN: {results[0]}")
print(f"LOSE: {results[1]}")
print(f"PUSH: {results[2]}")
print("====================")
print("Win PCT: {:.3f}%".format(results[0] / TRIALS * 100))
# Win percentage using optimal strategy without knowledge of the deck sequence is just under 50%.