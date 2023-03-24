'''
A step word is formed by taking a given word, adding a letter, and anagramming the result.
For example, starting with the word “APPLE”, you can add an “A” and anagram to get “APPEAL”.

Given a dictionary of words and an input word, create a function that returns all valid step words.
'''

from typing import List

class WordDiagram:
    def __init__(self, word: str):
        self.diagram = {}
        for letter in word:
            if letter not in self.diagram:
                self.diagram[letter] = 0
            self.diagram[letter] += 1

    def isStepWord(self, other):
        assert isinstance(other, WordDiagram)

        o_keys = sorted(other.diagram.keys())
        s_keys = sorted(self.diagram.keys())
        # Case where both words have the exact same type of letters.
        # Return true if and only if one letter appears one more time in the other word than in the self word.
        if o_keys == s_keys:
            found_1 = False

            for k in o_keys:
                diff = other.diagram[k] - self.diagram[k]
                if diff == 1 and found_1 == False:
                    found_1 = True
                elif diff != 0:
                    return False
                
            return found_1
        # Case where the other word has one additional letter type.
        # The new letter must only appear once in the other word, and all other letters must appear equally between words.
        elif len(set(o_keys).difference(set(s_keys))) == 1 and len(set(o_keys).intersection(set(s_keys))) == len(s_keys):
            for k in o_keys:
                if k not in s_keys:
                    if other.diagram[k] != 1:
                        return False
                elif other.diagram[k] != self.diagram[k]:
                    return False
                
            return True
        
        return False
    
# Memory-saving implementation.
def getStepWords(word: str, dictionary: List[str]):
    # Make a WordDiagram of the word, check against every word in the dictionary, and add if it's a matching step word.
    step_words = set()
    wd = WordDiagram(word)
    for target in dictionary:
        if wd.isStepWord(WordDiagram(target)):
            step_words.add(target)

    return step_words