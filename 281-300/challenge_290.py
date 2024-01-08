'''
On a mysterious island there are creatures known as Quxes which come in three colors: red, green, and blue.
One power of the Qux is that if two of them are standing next to each other, they can transform into a single creature of the third color.

Given N Quxes standing in a line, determine the smallest number of them remaining after any possible sequence of such transformations.

For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end up with a single Qux through the following steps:

        Arrangement       |   Change
----------------------------------------
['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
['B', 'B', 'G', 'B']      | (B, G) -> R
['B', 'R', 'B']           | (R, B) -> G
['B', 'G']                | (B, G) -> R
['R']                     |
'''

from typing import List

# Constant set.
_COLORS = {'R', 'G', 'B'}

# Helper function.
fusion = lambda c1, c2: list(_COLORS.difference(set([c1, c2])))[0]

# Recursive solution.
def minQuxes(qux_list: List[str]) -> int:
    def rMinQuxes(qux_list: List[str]):
        q_length = len(qux_list)
        for i in range(1, len(qux_list)):
            # Recur, replacing the current and previous colors with the fusion color when the current and previous positions don't match.
            if qux_list[i-1] != qux_list[i]:
                q_length = min(
                    q_length, 
                    rMinQuxes(qux_list[:i-1] + [fusion(qux_list[i-1], qux_list[i])] + qux_list[i+1:])
                )
            # At length of 1, quick return as this is the absolute minimum.
            if q_length == 1:
                return 1
        return q_length
    
    assert qux_list and all(map(lambda c: c in _COLORS, qux_list))
    return rMinQuxes(qux_list)

# Non-recursive solution.
def minQuxes2(qux_list: List[str]) -> int:
    out_list = []
    for q in qux_list:
        # Append current qux when list is empty or it matches the last color in out_list.
        if not out_list or out_list[-1] == q:
            out_list.append(q)
            continue
        # Pop the last qux and append the fused qux.
        out_list.append(fusion(q, out_list.pop()))
        # Fuse and add to out_list as long as the last two colors in out_list do not match.
        while len(out_list) > 1 and out_list[-1] != out_list[-2]:
            c1, c2 = out_list.pop(), out_list.pop()
            out_list.append(fusion(c1, c2))

    return len(out_list)

if __name__ == "__main__":
    print(minQuxes(['R', 'G', 'B', 'G', 'B'])) # 1
    print(minQuxes(['R', 'G', 'B'])) # 2
    print(minQuxes2(['R', 'G', 'B', 'G', 'B'])) # 1
    print(minQuxes2(['R', 'G', 'B'])) # 2