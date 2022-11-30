'''
Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome.
daily should return false, since there's no rearrangement that can form a palindrome.
'''

def canMakePalindrome(word: str):
    # Make a set that will include all characters that appear an odd number of times. Add when seen once, remove when seen twice, and so on.
    odd_chars = set()
    for char in word:
        if char in odd_chars:
            odd_chars.remove(char)
        else:
            odd_chars.add(char)

    # If more than one letter occurs an odd number of times, the word cannot form a palindrome in any permutation.
    return len(odd_chars) < 2

print(canMakePalindrome("carrace"))
print(canMakePalindrome("daily"))