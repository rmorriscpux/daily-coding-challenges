'''
The number 6174 is known as Kaprekar's constant, after the mathematician who discovered an associated property:
for all four-digit numbers with at least two distinct digits, repeatedly applying a simple procedure eventually results in this value.
The procedure is as follows:

For a given input x, create two new numbers that consist of the digits in x in ascending and descending order.
Subtract the smaller number from the larger number. For example, this algorithm terminates in three steps when starting from 1234:

4321 - 1234 = 3087
8730 - 0378 = 8352
8532 - 2358 = 6174
Write a function that returns how many steps this will take for a given input N.
'''

def stepsToKaprekar(x: int) -> int:
    assert x < 10000 and x > 0 # Positive integer that can be represented by four digits (incl. leading zeros)
    assert x % 1111 != 0 # Validates that at least two distinct digits exist in the integer.
    steps_count = 0
    while x != 6174: # End case - Kaprekar's constant
        # Separate the digits into a sorted list.
        digits = sorted([x//1000, (x//100) % 10, (x//10) % 10, x % 10])
        # Multiply digits by powers of 10 to get numbers with 4 digits rearranged in ascending and descending order.
        ascending = digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[3]
        descending = digits[3] * 1000 + digits[2] * 100 + digits[1] * 10 + digits[0]
        # Get new x value and increment steps_count.
        x = descending - ascending
        steps_count += 1
    return steps_count

if __name__ == "__main__":
    print(stepsToKaprekar(1234)) # 3