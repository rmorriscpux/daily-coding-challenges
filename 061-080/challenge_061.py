'''
Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
'''

def pow(x: int, y: int):
    # Universal Cases: 0^y = 0 where y > 0, 1 where y == 0, error where y < 0. x^0 = 1 where x >=0, -1 where x < 0.
    if x == 0:
        if y == 0:
            return 1
        elif y < 0:
            raise ZeroDivisionError
        return 0
    if y == 0:
        return 1 if x > 0 else -1

    power = 1
    result = x

    # Exponentially increase the result until we reach a point where doubling the exponent exceeds y.
    while power * 2 <= abs(y):
        result *= result
        power *= 2

    # Multiply in the remaining exponent via recursive call.
    result *= pow(x, abs(y)-power)

    # Negative power means inverse result.
    return 1/result if y < 0 else result

print(pow(2, 10)) # 1024
print(pow(10, 3)) # 1000
print(pow(3, 5))  # 243
print(pow(2, -3)) # 0.125

'''
Note: Naive solution would look like this:

result = 1
for i in range(0, abs(y)):
    result *= x

This solution works in O(N) time.
The doubling solution works in O(log N) time.
'''