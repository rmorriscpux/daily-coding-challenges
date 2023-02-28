'''
Let's define a “sevenish” number to be one which is either a power of 7, or the sum of unique powers of 7.
The first few sevenish numbers are 1, 7, 8, 49, and so on. Create an algorithm to find the nth sevenish number.
'''

def nthSevenishNumber(n: int):
    def rNthSevenishNumber(n_remaining, sevenish_numbers, starter):
        new_sevenish_numbers = []
        # All new_sevenish_numbers in each recursion are a sum of the current power of 7 and either one of the preceding sevenish numbers or 0.
        for num in sevenish_numbers:
            new_sevenish_numbers.append(starter + num)
            # Keep going until we reach n numbers, then return the last number calculated.
            n_remaining -= 1
            if n_remaining == 0:
                return new_sevenish_numbers[-1]

        # Continue with the new sevenish numbers included in the previous list and using the next power of 7.
        return rNthSevenishNumber(n_remaining, sevenish_numbers + new_sevenish_numbers, starter * 7)

    assert n > 0

    # Start with n, a list with a single 0 item, and 7^0 a.k.a. 1.
    return rNthSevenishNumber(n, [0], 1)

output = []
for i in range(1, 21):
    output.append(nthSevenishNumber(i))
print(output)