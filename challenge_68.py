'''
On our special chessboard, two bishops attack each other if they share the same diagonal.
This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M chessboard.
Write a function to count the number of pairs of bishops that attack each other.
The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).

For example, given M = 5 and the list of bishops:

(0, 0)
(1, 2)
(2, 2)
(4, 0)

The board would look like this:

[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]

You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.
'''

from typing import Tuple, Set

def bishopAttacks(bishops: Set[Tuple[int, int]], M: int):
    if M <= 0:
        raise ValueError("M must be positive.")

    count = 0

    attackable_positions = []
    for current_bishop in bishops:
        if (current_bishop[0] < 0 or current_bishop[0] >= M or
            current_bishop[1] < 0 or current_bishop[1] >= M):
            raise ValueError(f"Bishop position out of bounds: {current_bishop}, M={M}")

        # Determine if the current bishop is under threat from any previously placed bishops.
        # Note that the count is for the number of pairs of bishops that threaten each other, so we only count once.
        # Also that the current bishop can be under threat from more than one previously placed bishop.
        for bishop_threat in attackable_positions:
            if current_bishop in bishop_threat:
                count += 1

        # Now create a new set positions where the current bishop can move to on the board.
        can_move = set()

        # Northwest
        i, j = current_bishop[0]-1, current_bishop[1]-1
        while i >= 0 and j >= 0:
            can_move.add((i, j))
            i -= 1
            j -= 1

        # Northeast
        i, j = current_bishop[0]-1, current_bishop[1]+1
        while i >= 0 and j < M:
            can_move.add((i, j))
            i -= 1
            j += 1

        # Southeast
        i, j = current_bishop[0]+1, current_bishop[1]+1
        while i < M and j < M:
            can_move.add((i, j))
            i += 1
            j += 1

        # Southwest
        i, j = current_bishop[0]+1, current_bishop[1]-1
        while i < M and j >= 0:
            can_move.add((i, j))
            i += 1
            j -= 1

        # Add this set to the list containing each bishop's attackable positions.
        attackable_positions.append(can_move)

    return count

print(bishopAttacks({(0, 0), (1, 2), (2, 2), (4, 0)}, 5))