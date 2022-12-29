'''
Given a string s and a list of words words, where each word is the same length,
find all starting indices of substrings in s that is a concatenation of every word in words exactly once.

For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"], return [0, 13], since "dogcat" starts at index 0 and "catdog" starts at index 13.

Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return [] since there are no substrings composed of "dog" and "cat" in s.

The order of the indices does not matter.
'''

from typing import List

def findSubstringIndices(s: str, words: List[str]):
    def rFindSubstrings(s, words, word_length, index):
        if not words:
            return True

        if s[index:index+word_length] in words:
            words.remove(s[index:index+word_length])
            return rFindSubstrings(s, words, word_length, index+word_length)

        return False
        
    word_length = len(words[0])

    if not words or len(s) < word_length * len(words):
        return []

    starting_indices = []

    for index in range(0, len(s) - word_length * len(words) + 1):
        if s[index:index+word_length] in words and rFindSubstrings(s, words.copy(), word_length, index):
            starting_indices.append(index)

    return starting_indices

print(findSubstringIndices("dogcatcatcodecatdog", ["cat", "dog"]))
print(findSubstringIndices("barfoobazbitbyte", ["dog", "cat"]))