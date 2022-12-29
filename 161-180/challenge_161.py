'''
Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000, return 0000 1111 0000 1111 0000 1111 0000 1111.
'''

# Note: If the input integer is larger than 32 bits, the output will only represent the first 32 bits reversed.
def reverseInteger(num: int, as_binary: bool=False):
    MAX_INT = 0b11111111111111111111111111111111 # In decimal: 4294967295, or -2147483648 on 32-bit systems.
    reverse_num = (num & MAX_INT) ^ MAX_INT

    if as_binary:
        reverse_bin = bin(reverse_num)[2:]
        return reverse_bin.zfill(32)

    return reverse_num

print(reverseInteger(0))
print(reverseInteger(0b11110000111100001111000011110000, as_binary=True))