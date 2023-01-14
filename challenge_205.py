'''
Given an integer, find the next permutation of it in absolute order. For example, given 48975, the next permutation would be 49578.
'''

from bisect import bisect

def nextPermutation(num: int):
    # Case for one-digit integers, since only a single permutation exists.
    if num > -10 and num < 10:
        return num

    # Convert the integer into a list of digits.
    digit_list = []

    num_to_split = abs(num)
    while num_to_split != 0:
        digit_list.insert(0, num_to_split % 10)
        num_to_split //= 10

    # Find the first digit out of descending order, starting from the right. That number will be 
    replace_digit = None
    for i in range(len(digit_list)-2, -1, -1):
        if digit_list[i] < digit_list[i+1]:
            replace_digit = digit_list[i]
            break
    else:
        # Digits are all in descending order, so the number is the largest permutation already.
        return num

    # Reverse all digits to the right of the replace_digit in a new list.
    right_digits = digit_list[:i:-1]
    # Swap replace_digit and the next highest digit in right_digits.
    swap_index = bisect(right_digits, replace_digit)
    swap_digit = right_digits[swap_index]
    right_digits[swap_index] = replace_digit
    
    # Combine the digits: Digits to the left of the replace index, then the swap digit, then the right digits.
    out_num = 0
    for j in range(0, i):
        out_num += digit_list[j]
        out_num *= 10
    out_num += swap_digit
    for k in right_digits:
        out_num *= 10
        out_num += k
        
    return out_num if num > 0 else -out_num

print(nextPermutation(48975))
print(nextPermutation(-48975))