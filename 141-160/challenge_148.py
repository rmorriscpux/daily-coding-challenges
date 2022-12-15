'''
Gray code is a binary code where each successive value differ in only one bit, as well as when wrapping around.
Gray code is common in hardware so that we don't see temporary spurious values during transitions.

Given a number of bits n, generate a possible gray code for it.

For example, for n = 2, one gray code would be [00, 01, 11, 10].
'''

def grayCode(n: int):
    if n < 0:
        raise ValueError("n must be positive")

    if n == 0:
        return [""]

    next_lowest_gray_code = grayCode(n-1)

    first_half = ["0" + c for c in next_lowest_gray_code]
    second_half = ["1" + c for c in next_lowest_gray_code[::-1]]

    return first_half + second_half

print(grayCode(1))
print(grayCode(2))
print(grayCode(3))
print(grayCode(4))
print(grayCode(5))

def grayCodeInt(n: int):
    if n < 0:
        raise ValueError("n must be positive")

    if n == 0:
        return [0]

    next_lowest_gray_code = grayCodeInt(n-1)

    first_half = [num for num in next_lowest_gray_code]
    second_half = [2 ** (n-1) + num for num in next_lowest_gray_code[::-1]]

    return first_half + second_half

print(grayCodeInt(1))
print(grayCodeInt(2))
print(grayCodeInt(3))
print(grayCodeInt(4))
print(grayCodeInt(5))