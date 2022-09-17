'''
Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations.
You can assume b can only be 1 or 0.
'''

# i.e. No boolean / if-else logic.

def selectXorY(x: int, y: int, b: int):
    return x * b + y * abs(b-1)

print(selectXorY(10, 20, 1))
print(selectXorY(10, 20, 0))