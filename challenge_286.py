'''
The skyline of a city is composed of several buildings of various widths and heights, possibly overlapping one another when viewed from a distance.
We can represent the buildings using an array of (left, right, height) tuples, which tell us where on an imaginary x-axis a building begins and ends,
and how tall it is. The skyline itself can be described by a list of (x, height) tuples, giving the locations at which the height
visible to a distant observer changes, and each new height.

Given an array of buildings as described above, create a function that returns the skyline.

For example, suppose the input consists of the buildings [(0, 15, 3), (4, 11, 5), (19, 23, 4)].
In aggregate, these buildings would create a skyline that looks like the one below.

     ______  
    |      |        ___
 ___|      |___    |   | 
|   |   B  |   |   | C |
| A |      | A |   |   |
|   |      |   |   |   |
------------------------
As a result, your function should return [(0, 3), (4, 5), (11, 3), (15, 0), (19, 4), (23, 0)].
'''

from typing import List, Tuple

def getSkyline(buildings: List[Tuple[int, int, int]]) -> List[Tuple[int, int]]:
    def assertBuildings(buildings: List[Tuple[int, int, int]], start: int, end: int) -> None:
        assert start < end
        for b in buildings:
            assert b[0] < b[1]
            assert b[2] > 0
        return
    # Set start and end indices for building placement.
    start = min(map(lambda t: t[0], buildings))
    end = max(map(lambda t: t[1], buildings))
    # Optional assertion logic. (see above)
    assertBuildings(buildings, start, end)
    # Initialize array for building heights at each index, length equal to the delta between start and end.
    skyline_arr = [0 for i in range(end - start + 1)]
    # Loop through each building and place the max building height at each index.
    for b in buildings:
        for i in range(b[0] - start, b[1] - start):
            skyline_arr[i] = max(skyline_arr[i], b[2])
    # Build list of skyline tuples.
    skyline = [(start, skyline_arr[0])]
    # Add a new index & height tuple every time the height changes from the previous index.
    for i in range(1, len(skyline_arr)):
        if skyline_arr[i] != skyline_arr[i-1]:
            skyline.append((i + start, skyline_arr[i]))

    return skyline

if __name__ == "__main__":
    print(getSkyline([(0, 15, 3), (4, 11, 5), (19, 23, 4)]))