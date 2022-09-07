'''
Suppose you have a multiplication table that is N by N.
That is, a 2D array where the value at the i-th row and j-th column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).

Given integers N and X, write a function that returns the number of times X appears as a value in an N by N multiplication table.

For example, given N = 6 and X = 12, you should return 4, since the multiplication table looks like this:

| 1 | 2 | 3 | 4 | 5 | 6 |

| 2 | 4 | 6 | 8 | 10 | 12 |

| 3 | 6 | 9 | 12 | 15 | 18 |

| 4 | 8 | 12 | 16 | 20 | 24 |

| 5 | 10 | 15 | 20 | 25 | 30 |

| 6 | 12 | 18 | 24 | 30 | 36 |

And there are 4 12's in the table.
'''

from math import sqrt

# A multiplication table is symmetrical, as multiplication is a commutative operation (i.e. 3*5 = 5*3 = 15).
# Therefore we only need to determine whole multiples up to and including the square root of X.
# Add 2 to the count for every whole multiple found up to the square root, and 1 if the square root is a whole number.
def multCount(N: int, X: int):
    if N <= 0 or X <= 0:
        raise ValueError(f"N and X must be positive. N: {N}, X: {X}")
    count = 0
    sqrt_x = sqrt(X)

    # The number is guaranteed not to be in the multiplication table if its square root is greater than N.
    if sqrt_x > N:
        return count

    # Each number not on the diagonal axis will appear on opposite positions in the multiplication table. 
    # So add 2 to count for each we find a whole multiple of the product. Upper bound for multiples is N.
    multiple = 1
    while multiple < sqrt_x:
        if X % multiple == 0 and X / multiple <= N:
            count += 2
        multiple += 1

    # For square numbers, the product appears on the diagonal axis with no corresponding opposite. Therefore it should only be counted once.
    # We can tell X is square if its square root is a whole number.
    if sqrt_x == int(sqrt_x):
        count += 1

    return count

print(multCount(6, 12))
print(multCount(5, 12))
print(multCount(2, 8))
print(multCount(1, 1))
print(multCount(6, 4))
print(multCount(3, 6))