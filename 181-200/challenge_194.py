'''
Suppose you are given two lists of n points, one list p1, p2, ..., pn on the line y = 0 and the other list q1, q2, ..., qn on the line y = 1.
Imagine a set of n line segments connecting each point pi to qi. Write an algorithm to determine how many pairs of the line segments intersect.
'''

from typing import List

def intersectingLines(p: List[int], q: List[int]):
    n = min(len(p), len(q))

    intersecting_count = 0

    # Two line segments that end on the same horizontal axes intersect when the first line's top endpoint is to the left of the second line's top endpoint 
    # and the first line's bottom endpoint is to the right of the second line's bottom endpoint, or vice-versa.
    for i in range(0, n-1):
        for j in range(i+1, n):
            intersecting_count += int((p[i] < p[j] and q[i] > q[j]) or (p[i] > p[j] and q[i] < q[j])) # +1 if True, +0 if False.

    return intersecting_count

print(intersectingLines([1, 4, 5], [4, 2, 3]))
print(intersectingLines([1, 4, 5, 6, 8, 10, 12], [4, 2, 3, 4, 8, 9, 0]))
