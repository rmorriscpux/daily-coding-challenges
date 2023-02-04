'''
There are N prisoners standing in a circle, waiting to be executed. The executions are carried out starting with the kth person,
and removing every successive kth person going clockwise until there is no one left.

Given N and k, write an algorithm to determine where a prisoner should stand in order to be the last survivor.

For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3.

Bonus: Find an O(log N) solution if k = 2.
'''

def lastPrisoner(N: int, k: int):
    assert N > 0
    assert 0 <= k < N

    prisoners = [(i+1) for i in range(0, N)]
    index = k-1

    while len(prisoners) > 1:
        prisoners.pop(index)
        index = (index + k - 1) % len(prisoners)

    return prisoners[0]

print(lastPrisoner(5, 2))

def quickLastPrisoner(N: int):
    # k = 2
    assert N > 0

    prisoners = [(i+1) for i in range(0, N)]

    start = 0
    # Each iteration cuts the length of the prisoner list in half, so time complexity is O(log N)
    while len(prisoners) > 1:
        next_start = len(prisoners) % 2
        prisoners = prisoners[start::2]
        start = next_start

    return prisoners[0]

print(quickLastPrisoner(5))