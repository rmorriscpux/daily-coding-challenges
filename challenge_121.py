'''
Given a string which we can delete at most k, return whether you can make a palindrome.

For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.
'''

def canMakePalindrome(word: str, k: int):
    def rCanMakePalindrome(word, remaining_k, left, right):
        if left >= right:
            return True

        if word[left] == word[right]:
            return rCanMakePalindrome(word, remaining_k, left+1, right-1)
        elif remaining_k > 0:
            return rCanMakePalindrome(word, remaining_k-1, left+1, right) or rCanMakePalindrome(word, remaining_k-1, left, right-1)

        return False

    if len(word) == 0 or k < 0:
        return False

    return rCanMakePalindrome(word, k, 0, len(word)-1)

print(canMakePalindrome("waterrfetawx", 2))
print(canMakePalindrome("waterrfetawx", 1))