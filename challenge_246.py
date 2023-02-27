'''
Given a list of words, determine whether the words can be chained to form a circle.
A word X can be placed in front of another word Y in a circle if the last character of X is same as the first character of Y.

For example, the words ['chair', 'height', 'racket', 'touch', 'tunic'] can form the following circle: chair -> racket -> touch -> height -> tunic -> chair.
'''

from typing import List

def wordCircle(words: List[str]) -> bool:
    def rWordCircle(used: List[str], remaining: List[str]):
        if not remaining:
            # All words used. Return True if the last word's last letter matches the first word's first letter.
            return used[0][0] == used[-1][-1]
        
        for i, word in enumerate(remaining):
            # Recur into words where the first letter matches the last used word's last letter.
            if used[-1][-1] == word[0]:
                if rWordCircle(used + [word], remaining[:i] + remaining[i+1:]):
                    return True
                
        return False
    
    # Return False if the word list is empty or one or more word strings is empty.
    if not (words and all(words)):
        return False
    # Only need to recur using the first word in the list since a True result is circular.
    return rWordCircle([words[0]], words[1:])

print(wordCircle(['racket', 'chair', 'height', 'touch', 'tunic']))