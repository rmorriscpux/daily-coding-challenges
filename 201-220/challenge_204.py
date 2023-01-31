'''
Given a complete binary tree, count the number of nodes in faster than O(n) time.
Recall that a complete binary tree has every level filled except the last, and the nodes in the last level are filled starting from the left.
'''

from math import log2, floor # For helper function.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f"TreeNode({str(self.data)})"

def countCompleteTreeNodes(root: TreeNode):
    def rCountCompleteTreeNodes(root, l_count: int, r_count: int):
        if root == None:
            return 0
        # Count the steps it takes to go down the far left and the far right.
        if l_count == 0:
            node_ptr = root
            while node_ptr:
                node_ptr = node_ptr.left
                l_count += 1
        if r_count == 0:
            node_ptr = root
            while node_ptr:
                node_ptr = node_ptr.right
                r_count += 1

        if l_count == r_count:
            # Case where counts are equal on both sides. Total equals 1 subtracted from 2 to the power of the number of levels.
            return 2 ** l_count - 1
        else:
            # Case where counts are not equal.
            # At least either the left branch or right branch is fully balanced, ensuring that at least one side will recur only once.
            # Additionally, only one branch needs to be traversed in recurrences, further reducing calculation time.
            return 1 + rCountCompleteTreeNodes(root.left, l_count-1, 0) + rCountCompleteTreeNodes(root.right, 0, r_count-1)

    return rCountCompleteTreeNodes(root, 0, 0)

# Helper function that builds a 26-node complete binary tree.
def buildCompleteTree():
    LETTERS = 'abcdefghijklmnopqrstuvwxyz'

    root = None

    for i, letter in enumerate(LETTERS):
        level = floor(log2(i+1))

        if level == 0:
            root = TreeNode(letter)
            continue

        node_ptr = root
        for j in range(level-1, 0, -1):
            node_ptr = node_ptr.right if i+1 & 2**j else node_ptr.left

        if i+1 & 1:
            node_ptr.right = TreeNode(letter)
        else:
            node_ptr.left = TreeNode(letter)

    return root

root = buildCompleteTree()

print(countCompleteTreeNodes(root))