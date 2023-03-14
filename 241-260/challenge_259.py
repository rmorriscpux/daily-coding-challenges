'''
Ghost is a two-person word game where players alternate appending letters to a word.
The first person who spells out a word, or creates a prefix for which there is no possible continuation, loses.
Here is a sample game:

Player 1: g
Player 2: h
Player 1: o
Player 2: s
Player 1: t [loses]
Given a dictionary of words, determine the letters the first player should start with, such that with optimal play they cannot lose.

For example, if the dictionary is ["cat", "calf", "dog", "bear"], the only winning start letter would be b.
'''

from typing import List

def ghostOptimalPlay(words: List[str]):
    if not words:
        return set()
    
    lengths_per_letter = {}
    for word in words:
        if word[0] not in lengths_per_letter:
            lengths_per_letter[word[0]] = [0, 0]
        lengths_per_letter[word[0]][len(word)%2] += 1
    
    optimal_chars = set()
    for letter, lengths in lengths_per_letter.values():
        if lengths[1] == 0:
            optimal_chars.add(letter)
    
    return optimal_chars

