'''
Given a real number n, find the square root of n. For example, given n = 9, return 3.
'''

# Without using the built-in sqrt function in the math library.
# Since floating point numbers can be very long, determining the square root can also take a very long time.
# So set a tolerance so we get close enough without recurring for a long time.
TOLERANCE = 1e-6

def getSquareRoot(n):
    def rGetSquareRoot(n, start, end):
        mid = start + ((end-start) / 2)

        if n > mid * mid - TOLERANCE and n < mid * mid + TOLERANCE:
            return mid
        elif n > mid * mid:
            return rGetSquareRoot(n, mid, end)
        else:
            return rGetSquareRoot(n, start, mid)

    return rGetSquareRoot(n, 0, n)

print(getSquareRoot(10))