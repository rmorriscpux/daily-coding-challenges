'''
You are given given a list of rectangles represented by min and max x- and y-coordinates.
Compute whether or not a pair of rectangles overlap each other.
If one rectangle completely covers another, it is considered overlapping.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (0, 5),
    "dimensions": (4, 3)
}
return true as the first and third rectangle overlap each other.
'''

from typing import Tuple, List
from functools import cached_property # Supported in Python 3.8 and later only. Use @property decorator otherwise.

class Rectangle:
    def __init__(self, top_left: Tuple[int, int], dimensions: Tuple[int, int]):
        assert dimensions[0] > 0 and dimensions[1] > 0
        self.top_left = top_left
        self.width = dimensions[0]
        self.height = dimensions[1]

    @cached_property
    def area(self):
        return self.width * self.height

    @cached_property
    def bottom_right(self):
        return (self.top_left[0] + self.width, self.top_left[1] - self.height)

def overlapping(rectangles: List[dict]):
    def overlaps(r1: Rectangle, r2: Rectangle):
        right = r1.bottom_right[0] > r2.top_left[0] and r1.bottom_right[0] < r2.bottom_right[0]
        left = r1.top_left[0] > r2.top_left[0] and r1.top_left[0] < r2.bottom_right[0]
        bottom = r1.bottom_right[1] < r2.top_left[1] and r1.bottom_right[1] > r2.bottom_right[1]
        top = r1.top_left[1] < r2.top_left[1] and r1.top_left[1] > r2.bottom_right[1]
        
        return ((right and bottom) or (left and bottom) or (right and top) or (left and top) or
            ((right or left) and r1.top_left[1] == r2.top_left[1] and r1.bottom_right[1] == r2.bottom_right[1]) or
            ((top or bottom) and r1.top_left[0] == r2.top_left[0] and r2.bottom_right[0] == r2.bottom_right[0]))

    rect_list = []
    for r in rectangles:
        rect_list.append(Rectangle(r['top_left'], r['dimensions']))

    for i in range(0, len(rect_list)-1):
        for j in range(i+1, len(rect_list)):
            if (overlaps(rect_list[i], rect_list[j]) or overlaps(rect_list[j], rect_list[i])):
                return True

    return False

rectangles = [
    {
        "top_left": (1, 4),
        "dimensions": (3, 3) # width, height
    },
    {
        "top_left": (-1, 3),
        "dimensions": (2, 1)
    },
    {
        "top_left": (0, 5),
        "dimensions": (4, 3)
    }
]

print(overlapping(rectangles))

rectangles2 = [
    {
        "top_left": (1, 4),
        "dimensions": (3, 3) # width, height
    },
    {
        "top_left": (-1, 3),
        "dimensions": (2, 1)
    },
    {
        "top_left": (0, 10),
        "dimensions": (4, 3)
    }
]

print(overlapping(rectangles2))

rectangles3 = [
    {
        "top_left": (1, 4),
        "dimensions": (3, 3) # width, height
    },
    {
        "top_left": (-1, 3),
        "dimensions": (2, 1)
    },
    {
        "top_left": (2, 3),
        "dimensions": (1, 1)
    }
]

print(overlapping(rectangles3))