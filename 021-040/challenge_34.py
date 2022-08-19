'''
Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word.
If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome).
There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
'''

def makePalindrome(word):
    # Check if the word is already a palindrome. word[::-1] returns a reverse of the string.
    if word == word[::-1]:
        return word

    # Check edges
    if word[0] == word[-1]: # Edges are the same. Keep the same edges and go in.
        return word[0] + makePalindrome(word[1:-1]) + word[-1]
    else: # Edges are different. Make two new strings with one new edge on each end.
        new_word_1 = word[0] + makePalindrome(word[1:]) + word[0]
        new_word_2 = word[-1] + makePalindrome(word[:-1]) + word[-1]

        # Now return the shortest. If they're the same length, return the first alphabetically.
        if len(new_word_1) < len(new_word_2):
            return new_word_1
        elif len(new_word_1) > len(new_word_2):
            return new_word_2
        else:
            return new_word_1 if new_word_1 < new_word_2 else new_word_2

print(makePalindrome("race"))
print(makePalindrome("google"))
print(makePalindrome("googleel"))
print(makePalindrome("leelgoog"))