'''
Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".
'''

def longestPalindrome(s: str):
    # Terminator
    if len(s) <= 1:
        return None

    # This will work regardless of whether len(s) is odd or even.
    l_ptr = len(s) // 2 - 1
    r_ptr = len(s) - 1 - l_ptr

    # Go through and check that the palindrome is equal on both sides. Can break immediately if it's unequal.
    is_palindrome = True
    while l_ptr >= 0:
        if s[l_ptr] != s[r_ptr]:
            is_palindrome = False
            break
        l_ptr -= 1
        r_ptr += 1

    # Return if we have our palindrome.
    if is_palindrome:
        return s

    # Recur without last character.
    left_sub_s = longestPalindrome(s[:len(s)-1])
    right_sub_s = longestPalindrome(s[1:])

    if left_sub_s and right_sub_s:
        # Return the longest between left and right.
        return left_sub_s if len(left_sub_s) >= len(right_sub_s) else right_sub_s
    elif left_sub_s: # right_sub_s returned None
        return left_sub_s
    else: # left_sub_s returned None. Return right_sub_s regardless if it is a string or None.
        return right_sub_s

print(longestPalindrome("aabcdcb"))
print(longestPalindrome("bananas"))
print(longestPalindrome('abcdefg'))