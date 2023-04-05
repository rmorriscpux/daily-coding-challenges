'''
Write a function, throw_dice(N, faces, total), that determines how many ways it is possible to throw N dice with some number of faces each to get a specific total.

For example, throw_dice(3, 6, 7) should equal 15.
'''

def throwDice(N: int, faces: int, total: int) -> int:
    if N <= 0 or total not in range(N, N*faces+1):
        return 0
    if N == 1:
        return 1
    
    count = 0
    for roll in range(1, faces+1):
        count += throwDice(N-1, faces, total-roll)
    return count

print(throwDice(3, 6, 7))