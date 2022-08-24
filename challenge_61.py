'''
Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
'''

def pow(x: int, y: int):
    # Universal Cases: 0^y = 0; x^0 = 1 where x != 0.
    if x == 0:
        return 0
    if y == 0:
        return 1

    power = 1
    result = x

    # x^y = x^a * x^(y-2^a)
    while power * 2 <= abs(y):
        result *= result
        power *= 2

    result *= pow(x, abs(y)-power)

    # Negative power means inverse result.
    return 1/result if y < 0 else result

print(pow(2, 10))
print(pow(10, 3))
print(pow(3, 5))
print(pow(2, -3))