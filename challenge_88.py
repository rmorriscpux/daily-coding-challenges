'''
Implement division of two positive integers without using the division, multiplication, or modulus operators.
Return the quotient as an integer, ignoring the remainder.
'''

# This version also works for negative integers.
def intDivision(dividend: int, divisor: int):
    # Catch for dividing by zero.
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    # Quotient is negative if either the dividend or the divisor is negative, but not both.
    negative_quotient = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)

    # Total up the number of times we add the divisor until we reach the divident. That is the integer quotient.
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