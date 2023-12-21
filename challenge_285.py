'''
You are given an array representing the heights of neighboring buildings on a city street, from east to west.
The city assessor would like you to write an algorithm that returns how many of these buildings have a view of the setting sun,
in order to properly value the street.

For example, given the array [3, 7, 8, 3, 6, 1], you should return 3,
since the top floors of the buildings with heights 8, 6, and 1 all have an unobstructed view to the west.

Can you do this using just one forward pass through the array?
'''

from typing import List

def sunsetViewCount(building_heights: List[int]) -> int:
    assert building_heights
    # Initialize has_view list.
    has_view = []
    # Single forward pass through the building_heights array.
    for height in building_heights:
        # Work backwards removing any building from has_view with a height lower than the current building height.
        while has_view and has_view[-1] < height:
            has_view.pop()
        # Add the current building height to has_view.
        has_view.append(height)
    return len(has_view) # Number of buildings with a sunset view.

if __name__ == "__main__":
    print(sunsetViewCount([3, 7, 8, 3, 2, 6, 1])) # 3