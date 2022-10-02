'''
You are in an infinite 2D grid where you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)

You are given a sequence of points and the order in which you need to cover the points.
Give the minimum number of steps in which you can achieve it. You start from the first point.

Example: Input: [(0, 0), (1, 1), (1, 2)] Output: 2 It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
'''

from typing import List, Tuple

def numSteps(points: List[Tuple[int, int]]):
    # Based on the rules, the total steps between each successive point is the absolute value of ∆x or ∆y, whichever is larger.
    total_steps = 0
    for i in range(1, len(points)):
        total_steps += max(abs(points[i][0]-points[i-1][0]), abs(points[i][1]-points[i-1][1]))
    return total_steps

print(numSteps([(0, 0), (1, 1), (1, 2)]))
print(numSteps([(0, 0), (1, 1), (-1, -2)]))

'''
Additional Challenge:

Suppose that the order of points to travel to is not fixed. (i.e. we can start from any point and move to any unvisited point)
What would be the minimum number of steps needed to reach all points in the array?
'''

def numStepsUnordered(points: List[Tuple[int, int]]):
    def rNumStepsUnordered(start_point, remaining_points, total_steps):
        # End Case
        if not remaining_points:
            return total_steps

        # In each iteration of the recursive function we need to determine the following:
        # Minimum distance to any remaining point from the current start point.
        # Which remaining points are the minimum distance away. (Collect the indices for these points in remaining_points in a list)
        minimum_point_index_list = []
        min_step_count = float("inf")
        for index, end_point in enumerate(remaining_points):
            steps = max(abs(start_point[0]-end_point[0]), abs(start_point[1]-end_point[1]))
            if steps < min_step_count:
                # We have a new minimum step count. Reset minimum_point_index_list with the new index, removing everything before.
                min_step_count = steps
                minimum_point_index_list = [index]
            elif steps == min_step_count:
                minimum_point_index_list.append(index)

        # Get the result for every point that is the minimum distance away in the current iteration, and return the minimum from that.
        total_steps_map = map(lambda index: rNumStepsUnordered(remaining_points[index], remaining_points[:index]+remaining_points[index+1:], total_steps+min_step_count), minimum_point_index_list)
        return min(list(total_steps_map))

    return min(list(map(lambda index: rNumStepsUnordered(points[index], points[:index]+points[index+1:], 0), range(len(points)))))

print(numStepsUnordered([(0,0), (2,2), (3,0), (2,-2)]))
