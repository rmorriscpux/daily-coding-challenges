'''
Given a 32-bit positive integer N, determine whether it is a power of four in faster than O(log N) time.
'''

def isPowerOfFour(num: int):
    # Each 1 in the binary number represents a power of 4, from 4^0 = 1 to 4^15 = 1073741824.
    POWS_OF_FOUR_FILTER = int('0b01010101010101010101010101010101', base=2)
    # On bitwise and operations, powers of 2 and their negatives equal themselves, while all other numbers do not. 
    # Refer to two's complement notation for details. https://en.wikipedia.org/wiki/Two%27s_complement
    return (num & -num) & POWS_OF_FOUR_FILTER == num
    # Function runs in O(1) (constant) time.

print(isPowerOfFour(512))
print(isPowerOfFour(1024))
print(isPowerOfFour(1))
print(isPowerOfFour(2))
print(isPowerOfFour(12))