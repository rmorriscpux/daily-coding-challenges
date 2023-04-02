'''
The “look and say” sequence is defined as follows: beginning with the term 1,
each subsequent term visually describes the digits appearing in the previous term. The first few terms are as follows:

1
11
21
1211
111221
As an example, the fourth term is 1211, since the third term consists of one 2 and one 1.

Given an integer N, print the Nth term of this sequence.
'''

# Suggestion: For most programming languages, return a string term since integer representation is often bounded.
# Python has unbounded number representation, so the term returned here is an integer.

def lookAndSay(N: int):
    if N <= 0:
        raise ValueError("N must be positive.")
    # End Case
    if N == 1:
        return 1
    # Recur to get previous term to read.
    prev_term = str(lookAndSay(N-1))
    # Setup
    term = ""
    cur_digit = prev_term[0]
    appearances = 1
    for c in prev_term[1:]:
        if c == cur_digit:
            # Increment
            appearances += 1
        else:
            # Add appearance amount and the digit to the term string, then update cur_digit and reset appearances.
            term += str(appearances) + cur_digit
            cur_digit = c
            appearances = 1
    # Add final term.
    term += str(appearances) + cur_digit

    return int(term)

for i in range(1, 11):
    print(lookAndSay(i))