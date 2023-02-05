'''
You come across a dictionary of sorted words in a language you've never seen before.
Write a program that returns the correct order of letters in this language.

For example, given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'], you should return ['x', 'z', 'w', 'y'].
'''

from typing import List

def orderLetters(words: List[str]):
    def rOrderLetters(words: List[str], letters: dict):
        order = []
        new_words = {}
        prev_char = None

        for word in words:
            if word:
                char = word[0]
                if char != prev_char:
                    order.append(char)
                if char not in new_words:
                    new_words[char] = []
                new_words[char].append(word[1:])
                prev_char = char

        for i, char in enumerate(order):
            letters[char].update(order[i+1:])

        for char in new_words:
            rOrderLetters(new_words[char], letters)

        return

    def getPath(letters: dict, head: str, path: List[str]):
        if len(path) == len(letters):
            return path

        if not letters[head]:
            return None

        for next_head in letters[head]:
            new_path = getPath(letters, next_head, path + [next_head])
            if new_path:
                return new_path

    letters = {}
    for word in words:
        for letter in word:
            if letter not in letters:
                letters[letter] = set()

    rOrderLetters(words, letters)

    max_children = max(len(l_set) for l_set in letters.values())
    heads = [l for l in letters if len(letters[l]) == max_children]

    path = None
    for head in heads:
        path = getPath(letters, head, [head])
        if path:
            return path

    return

print(orderLetters(['xww', 'wxyz', 'wxyw', 'ywx', 'ywz']))