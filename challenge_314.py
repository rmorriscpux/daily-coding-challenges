'''
You are the technical director of WSPT radio, serving listeners nationwide.
For simplicity's sake we can consider each listener to live along a horizontal line stretching from 0 (west) to 1000 (east).

Given a list of N listeners, and a list of M radio towers, each placed at various locations along this line,
determine what the minimum broadcast range would have to be in order for each listener's home to be covered.

For example, suppose listeners = [1, 5, 11, 20], and towers = [4, 8, 15]. In this case the minimum range would be 5,
since that would be required for the tower at position 15 to reach the listener at position 20.
'''

def getMinRange(listeners: list[int], towers: list[int]) -> int:
    # The minimum range needed is equal to the maximum of all minimum distances between a listener and a tower.
    distances = dict()
    for l in listeners:
        distances[l] = min(map(lambda t: abs(l-t), towers))
    return max(distances.values())

if __name__ == "__main__":
    print(getMinRange([1, 5, 11, 20], [4, 8, 15]))