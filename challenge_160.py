'''
Given a tree where each edge has a weight, compute the length of the longest path in the tree.

For example, given the following tree:

   a
  /|\
 b c d
    / \
   e   f
  / \
 g   h

and the weights: a-b: 3, a-c: 5, a-d: 8, d-e: 2, d-f: 4, e-g: 1, e-h: 1, the longest path would be c -> a -> d -> f, with a length of 17.

The path does not have to pass through the root, and each node can have any amount of children.
'''

class TrieNode:
    def __init__(self, data, path_weight=None):
        if path_weight:
            assert isinstance(path_weight, int) and path_weight > 0
        
        self.data = data
        self.children = []
        self.path_weight = path_weight

    # Helper Print Methods
    def __repr__(self):
        return f"TrieNode({self.data} | Child Count: {len(self.children)})"

    def deepPrint(self):
        def rDeepPrint(trie_node, depth):
            indent = "" if depth == 0 else "|-".rjust(depth)
            weight = "" if not trie_node.path_weight else ": " + str(trie_node.path_weight)
            print(indent + trie_node.data + weight)
            for child in trie_node.children:
                rDeepPrint(child, depth+2)
            return

        rDeepPrint(self, 0)
        return

    # Method for adding a child to the trie node. The new node must have a path weight.
    def addChild(self, new_node):
        assert isinstance(new_node, TrieNode) and isinstance(new_node.path_weight, int)
        self.children.append(new_node)
        return self

# What needs to be determined from each node:
# - The longest singular path, including its own path weight.
# - The longest path through the node between two children, if applicable.
# - The longest path across its descendants, not counting the node, if applicable.

def longestPath(trie_root: TrieNode):
    def rLongestPath(trie_node: TrieNode):
        # Leaf
        if len(trie_node.children) == 0:
            sing_path = 0 if not trie_node.path_weight else trie_node.path_weight
            return sing_path, 0, 0

        # Singular child
        elif len(trie_node.children) == 1:
            last_sing_path, last_betw_path, last_desc_path = rLongestPath(trie_node.children[0])
            desc_path = max(last_betw_path, last_desc_path)
            sing_path = last_sing_path if not trie_node.path_weight else last_sing_path + trie_node.path_weight
            return sing_path, last_sing_path, desc_path

        # Multiple children
        max_betw_path, max_desc_path = 0, 0
        all_sing_paths = []

        for child in trie_node.children:
            child_sing_path, child_betw_path, child_desc_path = rLongestPath(child)
            max_desc_path = max(child_betw_path, child_desc_path, max_desc_path)
            all_sing_paths.append(child_sing_path)

        all_sing_paths.sort(reverse=True)

        max_betw_path = all_sing_paths[0] + all_sing_paths[1]
        cur_sing_path = all_sing_paths[0] if not trie_node.path_weight else all_sing_paths[0] + trie_node.path_weight

        return cur_sing_path, max_betw_path, max_desc_path

    return max(rLongestPath(trie_root))

root = TrieNode('a')
root.addChild(TrieNode('b', 3)).addChild(TrieNode('c', 5)).addChild(TrieNode('d', 8))
root.children[2].addChild(TrieNode('e', 2)).addChild(TrieNode('f', 4))
root.children[2].children[0].addChild(TrieNode('g', 1)).addChild(TrieNode('h', 1))

print(root)
root.deepPrint()
print(longestPath(root))