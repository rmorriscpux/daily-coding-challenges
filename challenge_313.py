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
    
def minMoves(target: Combo, deadends: set[Combo]=set(), start: Combo=Combo(0, 0, 0), prev_combos: set[Combo]=set({Combo(0, 0, 0)}), total_moves: int=0) -> int:
    if start == target:
        return total_moves
    if start in deadends:
        return None
    
    move_counts = []

    # n1
    n1_moves = set()
    n1_min_move_count = None
    # Leftwise
    next_n1 = start.n1
    next_n1_moves = set()
    while next_n1 != target.n1:
        next_n1 = (next_n1-1) % 10
        candidate = Combo(next_n1, start.n2, start.n3)
        if candidate in deadends:
            break
        if candidate not in prev_combos:
            next_n1_moves.add(candidate)
    for next_combo in n1_moves:
        moves_made = (start.n1 - next_combo.n1) % 10
        n1_move_count = minMoves(target, deadends, next_combo, prev_combos.union(n1_moves), total_moves + moves_made)
        if n1_move_count != None:
            if n1_min_move_count != None:
                n1_min_move_count = min(n1_move_count, n1_min_move_count)
            else:
                n1_min_move_count = n1_move_count
    # Rightwise
    next_n1 = start.n1
    next_n1_moves = set()
    while next_n1 != target.n1:
        next_n1 = (next_n1+1) % 10
        candidate = Combo(next_n1, start.n2, start.n3)
        if candidate in deadends:
            break
        if candidate not in prev_combos:
            next_n1_moves.add(candidate)
    for next_combo in n1_moves:
        moves_made = (next_combo.n1 - start.n1) % 10
        n1_move_count = minMoves(target, deadends, next_combo, prev_combos.union(n1_moves), total_moves + moves_made)
        if n1_move_count != None:
            if n1_min_move_count != None:
                n1_min_move_count = min(n1_move_count, n1_min_move_count)
            else:
                n1_min_move_count = n1_move_count
    if n1_min_move_count:
        move_counts.append(n1_min_move_count)
    
    # n2
    n2_moves = set()
    n2_min_move_count = None
    # Leftwise
    next_n2 = start.n2
    next_n2_moves = set()
    while next_n2 != target.n2:
        next_n2 = (next_n2-1) % 10
        candidate = Combo(next_n2, start.n2, start.n3)
        if candidate in deadends:
            break
        if candidate not in prev_combos:
            next_n2_moves.add(candidate)
    for next_combo in n2_moves:
        moves_made = (start.n2 - next_combo.n2) % 10
        n2_move_count = minMoves(target, deadends, next_combo, prev_combos.union(n2_moves), total_moves + moves_made)
        if n2_move_count != None:
            if n2_min_move_count != None:
                n2_min_move_count = min(n2_move_count, n2_min_move_count)
            else:
                n2_min_move_count = n2_move_count
    # Rightwise
    next_n2 = start.n2
    next_n2_moves = set()
    while next_n2 != target.n2:
        next_n2 = (next_n2+1) % 10
        candidate = Combo(next_n2, start.n2, start.n3)
        if candidate in deadends:
            break
        if candidate not in prev_combos:
            next_n2_moves.add(candidate)
    for next_combo in n2_moves:
        moves_made = (next_combo.n2 - start.n2) % 10
        n2_move_count = minMoves(target, deadends, next_combo, prev_combos.union(n2_moves), total_moves + moves_made)
        if n2_move_count != None:
            if n2_min_move_count != None:
                n2_min_move_count = min(n2_move_count, n2_min_move_count)
            else:
                n2_min_move_count = n2_move_count
    if n2_min_move_count:
        move_counts.append(n2_min_move_count)
    
    # n3
    n3_moves = set()
    n3_min_move_count = None
    # Leftwise
    next_n3 = start.n3
    next_n3_moves = set()
    while next_n3 != target.n3:
        next_n3 = (next_n3-1) % 10
        candidate = Combo(next_n3, start.n2, start.n3)
        if candidate in deadends:
            break
        if candidate not in prev_combos:
            next_n3_moves.add(candidate)
    for next_combo in n3_moves:
        moves_made = (start.n3 - next_combo.n3) % 10
        n3_move_count = minMoves(target, deadends, next_combo, prev_combos.union(n3_moves), total_moves + moves_made)
        if n3_move_count != None:
            if n3_min_move_count != None:
                n3_min_move_count = min(n3_move_count, n3_min_move_count)
            else:
                n3_min_move_count = n3_move_count
    # Rightwise
    next_n3 = start.n3
    next_n3_moves = set()
    while next_n3 != target.n3:
        next_n3 = (next_n3+1) % 10
        candidate = Combo(next_n3, start.n2, start.n3)
        if candidate in deadends:
            break
        if candidate not in prev_combos:
            next_n3_moves.add(candidate)
    for next_combo in n3_moves:
        moves_made = (next_combo.n3 - start.n3) % 10
        n3_move_count = minMoves(target, deadends, next_combo, prev_combos.union(n3_moves), total_moves + moves_made)
        if n3_move_count != None:
            if n3_min_move_count != None:
                n3_min_move_count = min(n3_move_count, n3_min_move_count)
            else:
                n3_min_move_count = n3_move_count
    if n3_min_move_count:
        move_counts.append(n3_min_move_count)
    
    if not move_counts:
        return None
    return min(move_counts)

if __name__ == "__main__":
    print(minMoves(Combo(4, 5, 6), {Combo(3, 4, 5), Combo(7, 6, 5)})) # 13
    print(minMoves(Combo(5, 5, 5), {Combo(4, 5, 5), Combo(6, 5, 5), Combo(5, 4, 5), Combo(5, 6, 5), Combo(5, 5, 4), Combo(5, 5, 6)})) # None