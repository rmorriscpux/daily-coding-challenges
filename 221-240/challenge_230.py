'''
You are given N identical eggs and access to a building with k floors.
Your task is to find the lowest floor that will cause an egg to break, if dropped from that floor. Once an egg breaks, it cannot be dropped again.
If an egg breaks when dropped from the xth floor, you can assume it will also break when dropped from any floor greater than x.

Write an algorithm that finds the minimum number of trial drops it will take, in the worst case, to identify this floor.

For example, if N = 1 and k = 5, we will need to try dropping the egg at every floor, beginning with the first,
until we reach the fifth floor, so our solution will be 5.
'''

def minDrops(N: int, k: int):
    assert N > 0 and k > 0

    case_matrix = [[float('inf') for j in range(0, k+1)] for i in range(0, N+1)]

    for floor in range(0, k+1):
        case_matrix[0][floor] = 0
        case_matrix[1][floor] = floor

    for egg in range(0, N+1):
        case_matrix[egg][0] = 0

    for floor in range(1, k+1):
        for egg in range(2, N+1):
            for i in range(1, floor+1):
                case_matrix[egg][floor] = min(case_matrix[egg][floor], 1 + max(case_matrix[egg-1][i-1], case_matrix[egg][floor-i]))

    return case_matrix[N][k]

print(minDrops(1, 5))
print(minDrops(2, 20))