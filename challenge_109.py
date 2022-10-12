'''
Given an unsigned 8-bit integer, swap its even and odd bits.
The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 should be 01010101. 11100010 should be 11010001.

Bonus: Can you do this in one line?
'''

# Notes and Breakdown:
# In Python, '0b' prefaces integers written in binary.
# The & (bitwise AND) with only even bits asserted and only odd bits asserted splits the input num into even and odd bits.
# The even bits are shifted left 1 position, and the odd bits are shifted right 1 position, swapping them.
# Finally, they are recombined using | (bitwise OR).
# A maximum of 8 bits (0-255 unsigned) are returned. In this, numbers represented with bits beyond the 8th are ignored.

swapEvenAndOddBits = lambda num: bin(((num & 0b01010101) << 1) | ((num & 0b10101010) >> 1))

print(swapEvenAndOddBits(0b11100010))
print(swapEvenAndOddBits(0b10101010))