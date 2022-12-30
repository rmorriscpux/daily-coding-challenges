'''
Given a string, split it into as few strings as possible such that each string is a palindrome.

For example, given the input string racecarannakayak, return ["racecar", "anna", "kayak"].

Given the input string abc, return ["a", "b", "c"].
'''

def palindromeSplit(palindrome_string: str):
    def rPalindromeSplit(palindrome_string, curr_string, found_palindromes):
        # Completed condition. Clean up any remaining letters in curr_string by converting to list.
        if not palindrome_string:
            return found_palindromes + list(curr_string)

        # Add to curr_string and check if it's a palindrome.
        curr_string += palindrome_string[0]
        result1 = rPalindromeSplit(palindrome_string[1:], curr_string, found_palindromes)
        result2 = None
        if curr_string == curr_string[::-1]:
            result2 = rPalindromeSplit(palindrome_string[1:], "", found_palindromes + [curr_string])

        # If we have a result2 and it has less palindromes than result1, return result2. Otherwise, return result1.
        return result2 if result2 and len(result1) > len(result2) else result1

    return rPalindromeSplit(palindrome_string, "", [])

print(palindromeSplit("racecarannakayak"))
print(palindromeSplit("abc"))