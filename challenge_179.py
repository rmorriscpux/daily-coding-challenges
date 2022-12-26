'''
Given the sequence of keys visited by a postorder traversal of a binary search tree, reconstruct the tree.

For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the following tree:

    5
   / \
  3   7
 / \   \
2   4   8
'''

from typing import List

class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

class BST:
    def __init__(self):
        self.root = None

    def __str__(self):
        def rStr(node):
            out_str = str(node.value)
            if node.left or node.right:
                out_str += "->["
                if node.left:
                    out_str += "left: " + rStr(node.left)
                if node.left and node.right:
                    out_str += "|"
                if node.right:
                    out_str += "right: " + rStr(node.right)
                out_str += "]"
            return out_str

        if not self.root:
            return ""

        return "BST(" + rStr(self.root) + ")"

    def addNode(self, value):
        def rAddNode(cur_node, value):
            if cur_node.value > value:
                if cur_node.left:
                    rAddNode(cur_node.left, value)
                else:
                    cur_node.left = TreeNode(value)
            elif cur_node.value < value:
                if cur_node.right:
                    rAddNode(cur_node.right, value)
                else:
                    cur_node.right = TreeNode(value)
            return

        if self.root:
            rAddNode(self.root, value)
        else:
            self.root = TreeNode(value)

        return self

    def postOrderTraversal(self):
        def rPostOrderTraversal(node, int_list):
            if node.left:
                rPostOrderTraversal(node.left, int_list)
            if node.right:
                rPostOrderTraversal(node.right, int_list)
            int_list.append(node.value)
            return

        int_list = []
        rPostOrderTraversal(self.root, int_list)
        return int_list

def rebuildPostorderedTree(int_list: List[int]):
    bst = BST()
    for num in int_list[::-1]:
        bst.addNode(num)

    return bst

in_bst = BST()
in_bst.addNode(5).addNode(7).addNode(8).addNode(3).addNode(4).addNode(2)
print(in_bst)
post_order = in_bst.postOrderTraversal()
print(post_order)
print(rebuildPostorderedTree(post_order))