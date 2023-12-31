'''
A competitive runner would like to create a route that starts and ends at his house,
with the condition that the route goes entirely uphill at first, and then entirely downhill.

Given a dictionary of places of the form {location: elevation}, and a dictionary mapping paths between
some of these locations to their corresponding distances, find the length of the shortest route satisfying the condition above.
Assume the runner's home is location 0.

For example, suppose you are given the following input:

elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
paths = {
    (0, 1): 10,
    (0, 2): 8,
    (0, 3): 15,
    (1, 3): 12,
    (2, 4): 10,
    (3, 4): 5,
    (3, 0): 17,
    (4, 0): 10
}

In this case, the shortest valid path would be 0 -> 2 -> 4 -> 0, with a distance of 28.
'''

import sys

def mapRoute(elevations: dict[int, int], paths: dict[tuple[int, int], int]) -> int:
    def rMapRoute(elevations: dict[int, int], c_paths: dict[int, dict[int, int]], cur_location: int, prev_distance: int, history: set[int]=set(), can_uphill: bool=True) -> int:
        if cur_location == 0:
            return prev_distance
        if cur_location in history:
            return sys.maxsize
        
        total_distance = sys.maxsize
        for next_location, distance in c_paths[cur_location].items():
            if elevations[next_location] > elevations[cur_location]:
                if can_uphill:
                    total_distance = min(total_distance, rMapRoute(elevations, c_paths, next_location, prev_distance + distance, history.union({cur_location}), True))
            elif elevations[next_location] == elevations[cur_location]:
                total_distance = min(total_distance, rMapRoute(elevations, c_paths, next_location, prev_distance + distance, history.union({cur_location}), can_uphill))
            else:
                total_distance = min(total_distance, rMapRoute(elevations, c_paths, next_location, prev_distance + distance, history.union({cur_location}), False))

        return total_distance

    c_paths = dict()
    for path, distance in paths.items():
        if path[0] not in c_paths:
            c_paths[path[0]] = dict()
        c_paths[path[0]][path[1]] = distance

    total_distance = sys.maxsize
    for next_location, distance in c_paths[0].items():
        if elevations[next_location] > elevations[0]:
            total_distance = min(total_distance, rMapRoute(elevations, c_paths, next_location, distance))

    return total_distance

if __name__ == "__main__":
    elevations = {
        0: 5, 
        1: 25, 
        2: 15, 
        3: 20, 
        4: 10}
    paths = {
        (0, 1): 10,
        (0, 2): 8,
        (0, 3): 15,
        (1, 3): 12,
        (2, 4): 10,
        (3, 4): 5,
        (3, 0): 17,
        (4, 0): 10
    }
    print(mapRoute(elevations, paths))