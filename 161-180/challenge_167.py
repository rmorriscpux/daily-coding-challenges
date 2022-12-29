'''
Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome.

For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].
'''

from typing import List

# I'm curious if there's a way to do this faster than O(N^2).

def findConcatenatedPalindromes(word_list: List[str]):
    palindrome_pairs = []

    # Because the indices need to be collected, do index iteration.
    for i in range(0, len(word_list)):
        for j in range(0, len(word_list)):
            # Do not combine a word with itself.
            if i == j:
                continue

            combined_word = word_list[i] + word_list[j]
            if combined_word == combined_word[::-1]:
                palindrome_pairs.append((i, j))

    return palindrome_pairs

print(findConcatenatedPalindromes(["code", "edoc", "da", "d", "mom"]))