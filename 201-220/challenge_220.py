'''
In front of you is a row of N coins, with values v_1, v_2, ..., v_n.

You are asked to play the following game. You and an opponent take turns choosing either the first or last coin from the row,
removing it from the row, and receiving the value of the coin.

Write a program that returns the maximum amount of money you can win with certainty, if you move first, assuming your opponent plays optimally.
'''

from typing import List

def getMaxCoinsValue(coins: List[int]):
    def rGetMaxCoinsValue(coins: List[int], p1_total: int, p1_turn: bool):
        # All coins removed, game end.
        if len(coins) == 0:
            return p1_total

        if p1_turn:
            # Compare the max results for each scenario for player 1.
            return max(rGetMaxCoinsValue(coins[1:], p1_total+coins[0], False), rGetMaxCoinsValue(coins[:-1], p1_total+coins[-1], False))
        else:
            # Player 2 always selects the higher coin between the two on the ends. Get max for player 1 when equal.
            if coins[0] == coins[1]:
                return max(rGetMaxCoinsValue(coins[1:], p1_total, True), rGetMaxCoinsValue(coins[:-1], p1_total, True))
            return rGetMaxCoinsValue(coins[1:], p1_total, True) if coins[0] > coins[-1] else rGetMaxCoinsValue(coins[:-1], p1_total, True)

    return rGetMaxCoinsValue(coins, 0, True)

print(getMaxCoinsValue([2, 4, 6, 8, 10, 1, 3, 5, 7, 9]))