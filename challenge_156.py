'''
Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given n = 13, return 2 since 13 = 3^2 + 2^2 = 9 + 4.

Given n = 27, return 3 since 27 = 3^2 + 3^2 + 3^2 = 9 + 9 + 9.
'''

def getMinSquares(num: int):
    def rGetMinSquares(num, squares):
        total_used = num // squares[0]
        remainder = num % squares[0]

        if remainder == 0:
            return total_used

        return total_used + rGetMinSquares(remainder, squares[1:])

    if num < 0:
        raise ValueError("num must be positive.")

    squares = []
    for square_root in range(1, num // 2):
        square = square_root ** 2
        if square > num:
            break
        squares.insert(0, square)

    return rGetMinSquares(num, squares)

print(getMinSquares(13))
print(getMinSquares(27))