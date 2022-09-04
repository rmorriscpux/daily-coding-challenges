'''
A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
'''

# The partial solution for single digit n reveals a pattern:
# Perfect number n is equal to (n * 10) + (10 - n)
# This breaks down for n with more than one digit.
# The quickest way to find the nth perfect number beyond this is to find integers with digits that sum up to 10 or less, up to the nth one,
# then multiply that integer by 10, and add the digit that will make all digits sum to 10, i.e. 10 - base_digit_sum.
# This is quicker than naively finding all numbers with digits that add up to 10 exactly.

def nthPerfectNumber(n: int):
    if n <= 0:
        raise ValueError("n must be positive.")

    perf_num_base = 0
    k = 0
    base_digit_sum = 0

    while k < n:
        perf_num_base += 1
        base_digit_sum = sum([int(digit) for digit in str(perf_num_base)])
        if base_digit_sum <= 10:
            k += 1

    return perf_num_base * 10 + 10 - base_digit_sum

print(nthPerfectNumber(1))
print(nthPerfectNumber(2))
print(nthPerfectNumber(12345))