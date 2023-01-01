'''
Given two rectangles on a 2D graph, return the area of their intersection. If the rectangles don't intersect, return 0.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}
and

{
    "top_left": (0, 5),
    "dimensions" (4, 3) # width, height
}
return 6.
'''

from typing import Tuple

class Rectangle:
    def __init__(self, top_left: Tuple[int, int], dimensions: Tuple[int, int]):
        assert dimensions[0] > 0 and dimensions[1] > 0
        self.top_left = top_left
        self.width = dimensions[0]
        self.height = dimensions[1]
        
    @property
    def bottom_right(self):
        return (self.top_left[0] + self.width, self.top_left[1] - self.height)

    @property
    def area(self):
        return self.width * self.height

def intersectionArea(r1: Rectangle, r2: Rectangle):
    # Returns true if the first rectangle completely surrounds the second rectangle.
    def envelopes(r_a: Rectangle, r_b: Rectangle):
        return (r_a.top_left[0] <= r_b.top_left[0] and r_a.top_left[1] >= r_b.top_left[1] and
            r_a.bottom_right[0] >= r_b.bottom_right[0] and r_a.bottom_right[1] <= r_b.bottom_right[1])

    def disjoint(r_a: Rectangle, r_b: Rectangle):
        return (r_a.bottom_right[1] > r_b.top_left[1] or r_b.bottom_right[1] > r_a.top_left[1] or
            r_a.top_left[0] > r_b.bottom_right[0] or r_b.top_left[0] > r_a.bottom_right[0])

    if envelopes(r1, r2):
        return r2.area

    if envelopes(r2, r1):
        return r1.area

    if disjoint(r1, r2) or disjoint(r2, r1):
        return 0

    heights = list(sorted([r1.top_left[1], r1.bottom_right[1], r2.top_left[1], r2.bottom_right[1]]))
    widths = list(sorted([r1.top_left[0], r1.bottom_right[0], r2.top_left[0], r2.bottom_right[0]]))
    height = heights[2] - heights[1]
    width = widths[2] - widths[1]

    return height * width

print(intersectionArea(Rectangle((1, 4), (3, 3)), Rectangle((0, 5), (4, 3))))