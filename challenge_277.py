'''
UTF-8 is a character encoding that maps each symbol to one, two, three, or four bytes.

For example, the Euro sign, €, corresponds to the three bytes 11100010 10000010 10101100. The rules for mapping characters are as follows:

For a single-byte character, the first bit must be zero.
For an n-byte character, the first byte starts with n ones and a zero. The other n - 1 bytes all start with 10. Visually, this can be represented as follows.
 Bytes   |           Byte format
-----------------------------------------------
   1     | 0xxxxxxx
   2     | 110xxxxx 10xxxxxx
   3     | 1110xxxx 10xxxxxx 10xxxxxx
   4     | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Write a program that takes in an array of integers representing byte values, and returns whether it is a valid UTF-8 encoding.
'''

from typing import List

BITMASK = {
    1: 128,
    2: 192,
    3: 224,
    4: 240,
    5: 248
}

def isValidUTF8(bytes: List[int]) -> bool:
    len_bytes = len(bytes)

    if len_bytes == 1:
        return not (bytes[0] & BITMASK[1])
    elif 2 <= len_bytes <= 4:
        return ((BITMASK[len_bytes+1] & bytes[0] == BITMASK[len_bytes]) and
                all(map(lambda b: BITMASK[2] & b == BITMASK[1], bytes[1:])))
    
    return False

print(isValidUTF8([77]))
print(isValidUTF8([177]))
print(isValidUTF8([200, 150]))
print(isValidUTF8([245, 191, 128, 177]))
print(isValidUTF8([200, 200]))
print(isValidUTF8([200, 191, 128, 177]))