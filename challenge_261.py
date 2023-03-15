'''
Huffman coding is a method of encoding characters based on their frequency.
Each letter is assigned a variable-length binary string, such as 0101 or 111110, where shorter lengths correspond to more common letters.
To accomplish this, a binary tree is built such that the path from the root to any leaf uniquely maps to a character. When traversing the path,
descending to a left child corresponds to a 0 in the prefix, while descending right corresponds to 1.

Here is an example tree (note that only the leaf nodes have letters):

        *
      /   \
    *       *
   / \     / \
  *   a   t   *
 /             \
c               s
With this encoding, cats would be represented as 0000110111.

Given a dictionary of character frequencies, build a Huffman tree, and use it to determine a mapping between characters and their encoded binary strings.
'''

from typing import Dict

from queue import Queue

class TreeNode:
    def __init__(self, character: str="*", freq: int=0):
        self.character = character
        self.left = None
        self.right = None
        self.freq = freq

def huffmanFromFrequencies(char_dict: Dict[str, int]):
    nodes = []
    for char, freq in char_dict.items():
        nodes.append(TreeNode(char, freq))
    nodes.sort(key=lambda n: n.freq)

    if not nodes:
        return TreeNode()
    
    while len(nodes) > 1:
        n1 = nodes.pop(0)
        n2 = nodes.pop(0)

        connect = TreeNode(freq=n1.freq+n2.freq)
        connect.left = n1
        connect.right = n2

        nodes.append(connect)

    return nodes[0]

def huffmanMapping(*words: str):
    def rHuffmanMapping(cur_node: TreeNode, huff_map: Dict[str, str], huff_code: str=""):
        if cur_node.character != "*":
            huff_map[cur_node.character] = huff_code
            return
        
        if cur_node.left:
            rHuffmanMapping(cur_node.left, huff_map, huff_code + '0')
        if cur_node.right:
            rHuffmanMapping(cur_node.right, huff_map, huff_code + '1')

        return

    if not words:
        return {}
    
    char_freq_map = {}

    for word in words:
        for char in word.lower():
            if char not in char_freq_map:
                char_freq_map[char] = 0
            char_freq_map[char] += 1
    
    huffman_tree = huffmanFromFrequencies(char_freq_map)

    huff_map = {}
    rHuffmanMapping(huffman_tree, huff_map)

    return huff_map

print(huffmanMapping("cats", "cars", "dogs"))
print(huffmanMapping("cats", "cars"))
print(huffmanMapping("cats"))