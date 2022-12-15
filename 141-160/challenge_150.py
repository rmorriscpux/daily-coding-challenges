'''
Given a list of points, a central point, and an integer k, find the nearest k points from the central point.

For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point (1, 2), and k = 2, return [(0, 0), (3, 1)].
'''

from typing import List, Tuple

def getNearestKPoints(points_list: List[Tuple[int, int]], central_point: Tuple[int, int], k: int):
    if k <= 0:
        return []
    
    # Calculate the distance of each point from central_point, and sort the indices by these distances.
    # Distance is calculated using the formula a^2 + b^2 = c^2. So square the x and y deltas and sum them; we can omit taking the square root of that sum.
    distance_list = []
    for i, point in enumerate(points_list):
        distance_list.append((i, (point[0] - central_point[0]) ** 2 + (point[1] - central_point[1]) ** 2))
    distance_list.sort(key=lambda p : p[1])

    # Now based on the distance_list, get the cooresponding points in the points_list.
    out_list = []
    for i, (index, dist) in enumerate(distance_list):
        if i == k:
            break
        out_list.append(points_list[index])

    return out_list

print(getNearestKPoints([(0, 0), (5, 4), (3, 1)], (1, 2), 2))