'''
Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.

A solution will always exist. See Goldbach's conjecture.

Example:

Input: 4 Output: 2 + 2 = 4 If there are more than one solution possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then
    [a, b] < [c, d]
    if a < c or a==c and b < d.
'''

from math import sqrt

def findPrimeAdditives(sum_value: int):
    if sum_value <= 2 or sum_value % 2 != 0:
        raise ValueError("sum_value must be an even integer greater than 2.")

    # Helper function to determine if a number is prime.
    def isPrime(num):
        for i in range(2, int(sqrt(num))+1):
            if num % i == 0:
                return False
        return True

    # Edge case that the below loop won't catch.
    if sum_value == 4:
        return 2, 2

    # Goes through odd numbers in descending order to check if they are prime, down to half the input value.
    # Then check if the difference is also prime. If so, we have the first lexiconigraphical solution.
    for add_value in range(sum_value-3, sum_value//2-1, -2):
        if isPrime(add_value):
            if isPrime(sum_value-add_value):
                return sum_value-add_value, add_value

    return 1, sum_value-1 # Shouldn't get here. Note: 1 is not prime.

print(findPrimeAdditives(123456))