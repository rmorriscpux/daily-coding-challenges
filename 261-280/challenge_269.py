'''
You are given an string representing the initial conditions of some dominoes. Each element can take one of three values:

L, meaning the domino has just been pushed to the left,
R, meaning the domino has just been pushed to the right, or
., meaning the domino is standing still.
Determine the orientation of each tile when the dominoes stop falling.
Note that if a domino receives a force from the left and right side simultaneously, it will remain upright.

For example, given the string .L.R....L, you should return LL.RRRLLL.

Given the string ..R...L.L, you should return ..RR.LLLL.
'''

from typing import List

def dominoes(start_state: str) -> str:
    def rDominoes(cur_state: List[str]):
        next_state = cur_state.copy()
        if cur_state[0] == '.' and cur_state[1] == 'L':
            next_state[0] = 'L'
        if cur_state[-1] == '.' and cur_state[-2] == 'R':
            next_state[-1] = 'R'
        for i in range(1, len(cur_state)-1):
            if cur_state[i] == '.':
                if cur_state[i-1] == 'R' and cur_state[i+1] != 'L':
                    next_state[i] = 'R'
                elif cur_state[i+1] == 'L' and cur_state[i-1] != 'R':
                    next_state[i] = 'L'
        return "".join(cur_state) if cur_state == next_state else rDominoes(next_state)
    
    assert all(map(lambda c: c in "LR.", start_state))

    if len(start_state) <= 1:
        return start_state
    
    return rDominoes(list(start_state))

print(dominoes(".L.R....L"))
print(dominoes("..R...L.L"))