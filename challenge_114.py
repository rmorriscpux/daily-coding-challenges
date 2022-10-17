'''
Given a string and a set of delimiters, reverse the words in the string while maintaining the relative order of the delimiters.
For example, given “hello/world:here”, return “here/world:hello”

Follow-up: Does your solution work for the following cases: “hello/world:here/”, “hello//world:here”
'''

from typing import Set

def reverseStringWithDelimiters(word_string: str, delimiters: Set[str]):
    words, spaces = [], []

    # Determine if the string starts with a delimiter or not.
    on_word = word_string[0] not in delimiters
    new_word = ""

    # Build two lists, one with words, one with delimiters (spaces)
    for i in range(0, len(word_string)):
        if word_string[i] in delimiters and on_word:
            words.insert(0, new_word)
            new_word = ""
            on_word = False
        elif not (word_string[i] in delimiters or on_word):
            spaces.append(new_word)
            new_word = ""
            on_word = True

        new_word += word_string[i]
    # Catch last word/space.
    if on_word:
        words.insert(0, new_word)
    else:
        spaces.append(new_word)

    # Now zipper merge the two lists into a single string and return.
    out_str = ""
    on_word = word_string[0] not in delimiters
    for i in range(0, len(words) + len(spaces)):
        if on_word:
            out_str += words[i//2]
        else:
            out_str += spaces[i//2]
        on_word = not on_word

    return out_str

print(reverseStringWithDelimiters("hello/world:here", {"/", ":"}))
print(reverseStringWithDelimiters("hello/world:here/", {"/", ":"}))
print(reverseStringWithDelimiters("hello//world:here", {"/", ":"}))