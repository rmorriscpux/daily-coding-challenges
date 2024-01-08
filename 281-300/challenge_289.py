'''
The game of Nim is played as follows. Starting with three heaps, each containing a variable number of items,
two players take turns removing one or more items from a single pile. The player who eventually is forced to take the last stone loses.
For example, if the initial heap sizes are 3, 4, and 5, a game could be played as shown below:

A	B	C
3	4	5
3	1	5
3	1	3
0	1	3
0	1	0
0	0	0
In other words, to start, the first player takes three items from pile B. The second player responds by removing two stones from pile C.
The game continues in this way until player one takes last stone and loses.

Given a list of non-zero starting values [a, b, c], and assuming optimal play, determine whether the first player has a forced win.
'''

# In Nim, the optimal strategy is to take items from a heap such that the bitwise XOR across all heaps = 0.
# As long as this can be done on the first move, the first player will always win with optimal play.
# See https://en.wikipedia.org/wiki/Nim for details.

from typing import List

def hasForcedWin(heaps: List[int]) -> bool:
    # Assert all positive integers in non-empty list.
    assert heaps
    assert all(map(lambda i: i > 0, heaps))
    # Misere rule: Player who takes the last item loses. A special case needs to be made for when all heaps contain just 1 item.
    if all(map(lambda i: i == 1, heaps)):
        return not(len(heaps) % 2) # True if number of heaps is even, False if number of heaps is odd.
    # Get bitwise XOR value of the initial state.
    xor_val = 0
    for h in heaps:
        xor_val ^= h
    # If the XOR of xor_val and a given heap is less than the total items in that heap,
    # then it is possible to remove items from that heap such that the overall XOR value of all heaps is 0.
    for h in heaps:
        if xor_val ^ h < h:
            return True
        
    return False

if __name__ == "__main__":
    print(hasForcedWin([3, 4, 5])) # True
    print(hasForcedWin([3, 4, 7])) # False