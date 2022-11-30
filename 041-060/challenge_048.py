'''
Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g
'''

from typing import List

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        out_str = str(self.data)
        if self.left:
            out_str += f", [left: {repr(self.left)}]"
        if self.right:
            out_str += f", [right: {repr(self.right)}]"
        return out_str

def buildTree(pre_order: List, in_order: List):
    if not pre_order or not in_order:
        return None

    root = TreeNode(pre_order[0])
    
    if len(pre_order) == 1:
        return root

    for i in range(0, len(in_order)):
        if in_order[i] == root.data:
            root.left = buildTree(pre_order[1:i+1], in_order[:i])
            root.right = buildTree(pre_order[i+1:], in_order[i+1:])

    return root

def printTreeInOrder(root: TreeNode):
    def getTreeAsList(node: TreeNode, tree_list: List):
        if node.left:
            getTreeAsList(node.left, tree_list)
        tree_list.append(node.data)
        if node.right:
            getTreeAsList(node.right, tree_list)

        return

    tree_list = []
    getTreeAsList(root, tree_list)

    print(tree_list)

    return

def printTreePreOrder(root: TreeNode):
    def getTreePreOrder(node: TreeNode, tree_list: List):
        tree_list.append(node.data)
        if node.left:
            getTreePreOrder(node.left, tree_list)
        if node.right:
            getTreePreOrder(node.right, tree_list)

        return

    tree_list = []
    getTreePreOrder(root, tree_list)

    print(tree_list)

    return

t = buildTree(['a', 'b', 'd', 'e', 'c', 'f', 'g'], ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
print(t)
printTreeInOrder(t)
printTreePreOrder(t)