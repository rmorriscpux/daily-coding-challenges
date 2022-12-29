'''
Given a list of words, return the shortest unique prefix of each word. For example, given the list:

    dog
    cat
    apple
    apricot
    fish

Return the list:

    d
    c
    app
    apr
    f
'''

from typing import List

class TrieNode:
    def __init__(self, letter="", parent=None):
        self.letter = letter
        self.word = None
        self.next_letters = {}
        self.parent = parent
    
    def __repr__(self):
        return self.letter

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str):
        def rAddWord(trie_node: TrieNode, word: str, letter_index: int):
            if letter_index == len(word):
                trie_node.word = word
                return

            if word[letter_index] not in trie_node.next_letters:
                trie_node.next_letters[word[letter_index]] = TrieNode(word[letter_index], trie_node)

            rAddWord(trie_node.next_letters[word[letter_index]], word, letter_index+1)

            return

        rAddWord(self.root, word, 0)

        return

    def getUniquePrefix(self, word: str):
        def getTargetWordNode(cur_node: TrieNode, word, letter_index: int):
            if cur_node.word == word:
                return cur_node

            if letter_index >= len(word) or word[letter_index] not in cur_node.next_letters:
                raise ValueError(f"Word {word} Not Found")

            return getTargetWordNode(cur_node.next_letters[word[letter_index]], word, letter_index+1)

        if word == "":
            return ""

        node_ptr = getTargetWordNode(self.root, word, 0)

        # If there are any children, the unique prefix is the full word.
        if node_ptr.next_letters:
            return word

        # Backtrack until the parent node has no parent, has more than 1 child, or contains a word.
        prefix_length = len(word)
        while node_ptr != self.root:
            if (not node_ptr.parent.parent or
                len(node_ptr.parent.next_letters) > 1 or
                node_ptr.parent.word):
                return word[:prefix_length]

            prefix_length -= 1
            node_ptr = node_ptr.parent

        return ""

def getAllUniquePrefixes(word_list: List[str]):
    # Build Trie
    word_trie = Trie()
    for word in word_list:
        word_trie.addWord(word)

    unique_prefixes = []
    
    for word in word_list:
        unique_prefixes.append(word_trie.getUniquePrefix(word))

    return unique_prefixes

print(getAllUniquePrefixes(["dog", "cat", "apple", "applesauce", "apricot", "fish"]))