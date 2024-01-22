'''
You are given a circular lock with three wheels, each of which display the numbers 0 through 9 in order.
Each of these wheels rotate clockwise and counterclockwise.

In addition, the lock has a certain number of “dead ends”, meaning that if you turn the wheels to one of these combinations,
the lock becomes stuck in that state and cannot be opened.

Let us consider a “move” to be a rotation of a single wheel by one digit, in either direction.
Given a lock initially set to 000, a target combination, and a list of dead ends,
write a function that returns the minimum number of moves required to reach the target state, or None if this is impossible.
'''

from typing import NamedTuple

class Combo(NamedTuple):
    n1: int
    n2: int
    n3: int
    
def minMoves(target: Combo, deadends: set[Combo]=set(), start: Combo=Combo(0, 0, 0), prev_combos: set[Combo]=set(), total_moves: int=0) -> int:
    if start == target:
        return total_moves
    if start in deadends:
        return None
    
    move_set = []

    prev_combos.add(start)
    if start.n1 != target.n1:
        left_move, right_move = Combo((start.n1-1)%10, start.n2, start.n3), Combo((start.n1+1)%10, start.n2, start.n3)
        if left_move not in prev_combos:
            move_set.append(minMoves(target, deadends, left_move, prev_combos, total_moves+1))
        if right_move not in prev_combos:
            move_set.append(minMoves(target, deadends, right_move, prev_combos, total_moves+1))
            
    if start.n2 != target.n2:
        left_move, right_move = Combo(start.n1, (start.n2-1)%10, start.n3), Combo(start.n1, (start.n2+1)%10, start.n3)
        if left_move not in prev_combos:
            move_set.append(minMoves(target, deadends, left_move, prev_combos, total_moves+1))
        if right_move not in prev_combos:
            move_set.append(minMoves(target, deadends, right_move, prev_combos, total_moves+1))
            
    if start.n3 != target.n3:
        left_move, right_move = Combo(start.n1, start.n2, (start.n3-1)%10), Combo(start.n1, start.n2, (start.n3+1)%10)
        if left_move not in prev_combos:
            move_set.append(minMoves(target, deadends, left_move, prev_combos, total_moves+1))
        if right_move not in prev_combos:
            move_set.append(minMoves(target, deadends, right_move, prev_combos, total_moves+1))

    prev_combos.remove(start)

    move_set = [move for move in move_set if move != None]

    if not move_set:
        return None
    
    return min(move_set)

if __name__ == "__main__":
    print(minMoves(Combo(4, 5, 6), {Combo(3, 4, 5), Combo(7, 6, 5)})) # 15
    print(minMoves(Combo(5, 5, 5), {Combo(4, 5, 5), Combo(6, 5, 5), Combo(5, 4, 5), Combo(5, 6, 5), Combo(5, 5, 4), Combo(5, 5, 6)})) # None