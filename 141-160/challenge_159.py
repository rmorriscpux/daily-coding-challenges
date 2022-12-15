'''
Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
'''

def firstRecurringCharacter(word: str):
    chars_found = set()
    # Traverse through every character in word, add it to the set if it's not in the set. If it is in the set, return that character.
    for char in word:
        if char in chars_found:
            return char
        else:
            chars_found.add(char)
    # No recurring characters.
    return None

print(firstRecurringCharacter("acbbac"))
print(firstRecurringCharacter("abcdef"))