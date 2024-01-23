'''
Write an algorithm that finds the total number of set bits in all integers between 1 and N.
'''

# Two funtions representing a slow, simple implementation. For comparison purposes. Time complexity is O(N^2).
def bitCount(N: int) -> int:
    assert N >= 0
    count = 0
    while N > 0:
        count += N % 2
        N >>= 1
    return count

def setBitTotalExh(N: int) -> int:
    count = 0
    for i in range(1, N+1):
        count += bitCount(i)
    return count

# Quicker implementation done in O(log2(N)) time.
def setBitTotal(N: int) -> int:
    if N <= 0:
        return 0
    # For whole powers of 2 with an integer 'exponent' (1, 2, 4, 8...), only one bit is set when represented in binary. ex: 2^5 = 32 = 0b100000.
    # The sum of set bits in each position for every positive integer before 2^(exponent-1). Multiply this by exponent to represent every position.
    # 'diff' represents the remainder of N after 2^(exponent). For this, recur with diff as the new parameter,
    # and add diff to represent every instance of a set bit in the leftmost position.
    exponent = 0
    diff = N - 2 ** exponent
    while diff >= 2 ** exponent:
        exponent += 1
        diff = N - 2 ** exponent

    count = 1 + int(2 ** (exponent - 1)) * exponent + diff + setBitTotal(diff)

    return count

if __name__ == "__main__":
    for i in range(1, 21):
        print(i, bitCount(i), setBitTotalExh(i), setBitTotal(i))