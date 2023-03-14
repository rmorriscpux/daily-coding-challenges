'''
A cryptarithmetic puzzle is a mathematical game where the digits of some numbers are represented by letters. Each letter represents a unique digit.

For example, a puzzle of the form:

  SEND
+ MORE
--------
 MONEY
may have the solution:

{'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O', 0, 'R': 8, 'Y': 2}
Given a three-word puzzle like the one above, create an algorithm that finds a solution.
'''

from typing import Set

def cryptarithmetic(word1: str, word2: str, sum_word: str) -> dict:
    def numFromWord(char_map: dict, word: str):
        digit_factor = 1
        number = 0
        for letter in reversed(word):
            number += char_map[letter] * digit_factor
            digit_factor *= 10
        return number
    
    def isValidMap(char_map: dict, word1: str, word2: str, sum_word: str):
        return numFromWord(char_map, word1) + numFromWord(char_map, word2) == numFromWord(char_map, sum_word)
    
    def assignLetters(letters_left: Set[str], nums_left: Set[int], not_available: dict, letter_map: dict):
        if not letters_left:
            return [letter_map]
        
        current_letter = list(letters_left)[0]
        letter_maps = []

        for num in nums_left:
            if num in not_available[current_letter]:
                continue

            new_letter_map = letter_map.copy()
            new_letter_map[current_letter] = num
            
            next_letter_maps = assignLetters(letters_left.difference({current_letter}), nums_left.difference({num}), not_available, new_letter_map)
            letter_maps.extend(next_letter_maps)
        
        return letter_maps

    letters = set(word1).union(set(word2), set(sum_word))
    if len(letters) > 10:
        raise ValueError("More letters than digits.")
    numbers = set(range(0, 10))

    not_available = {}
    for l in letters:
        not_available[l] = set()
    not_available[word1[0]].add(0)
    not_available[word2[0]].add(0)
    not_available[sum_word[0]].add(0)

    letter_maps = assignLetters(letters, numbers, not_available, {})

    for l_m in letter_maps:
        if isValidMap(l_m, word1, word2, sum_word):
            return l_m
        
    return {}

print(cryptarithmetic("SEND", "MORE", "MONEY"))