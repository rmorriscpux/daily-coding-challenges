'''
Implement division of two positive integers without using the division, multiplication, or modulus operators.
Return the quotient as an integer, ignoring the remainder.
'''

def intDivision(dividend: int, divisor: int):
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    negative_quotient = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)

    quotient = 0
    added_divisors = 0

    while (added_divisors + abs(divisor) <= abs(dividend)):
        quotient += 1
        added_divisors += abs(divisor)

    return -quotient if negative_quotient else quotient

print(intDivision(11, 3))
print(intDivision(11, -3))
print(intDivision(-11, 3))
print(intDivision(-11, -3))
# print(intDivision(11, 0))