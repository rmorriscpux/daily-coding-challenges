'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
Assume that each node in the tree also has a pointer to its parent.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined betweentwo nodes v and w
as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
'''

from math import floor

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"<TreeNode Value: {self.value}, Left: {repr(self.left)}, Right: {repr(self.right)}>"

class BSTree:
    def __init__(self, *args):
        self.root = None

        for value in args:
            self.addNode(value)

    # Adds a node to the tree if the value does not exist in the tree.
    def addNode(self, value):
        def rAddNode(node_ptr, value):
            if value < node_ptr.value:
                if node_ptr.left:
                    rAddNode(node_ptr.left, value)
                else:
                    node_ptr.left = TreeNode(value)
                    node_ptr.left.parent = node_ptr
            elif value > node_ptr.value:
                if node_ptr.right:
                    rAddNode(node_ptr.right, value)
                else:
                    node_ptr.right = TreeNode(value)
                    node_ptr.right.parent = node_ptr
            return

        if self.root:
            rAddNode(self.root, value)
        else:
            self.root = TreeNode(value)

        return self

    # Searches for a value in the tree and returns the node with that value property.
    def findNode(self, value):
        def rFindNode(node_ptr, value):
            if node_ptr == None:
                return None
            if value == node_ptr.value:
                return node_ptr
            elif value < node_ptr.value:
                return rFindNode(node_ptr.left, value)
            else:
                return rFindNode(node_ptr.right, value)

        return rFindNode(self.root, value)

    # # Searches for a value in the tree and removes it, reshaping the tree to maintain its binary search property.
    # def removeNode(self, value):
    #     def moveFromLeft(node_ptr, dest_node):
    #         if node_ptr.right: # Going recursively to the rightmost node. Return immediately afterward.
    #             moveFromLeft(node_ptr.right, dest_node)
    #             return
            
    #         # Once at the node we need, put the current node's value into the destination node.
    #         dest_node.value = node_ptr.value

    #         # Afterward, we have to keep going if the current node has any children on the left. If not, delete the current node.
    #         if node_ptr.left:
    #             moveFromLeft(node_ptr.left, node_ptr)
    #         else:
    #             del node_ptr

    #         return

    #     # Same as above, but in reverse.
    #     def moveFromRight(node_ptr, dest_node):
    #         if node_ptr.left:
    #             moveFromRight(node_ptr.left, dest_node)
    #             return

    #         dest_node.value = node_ptr.value

    #         if node_ptr.right:
    #             moveFromRight(node_ptr.right, node_ptr)
    #         else:
    #             del node_ptr

    #         return

    #     del_node = self.findNode(value)
    #     # Value not found in tree.
    #     if not del_node:
    #         return None

    #     if del_node.left: # Select the rightmost node on the left branch and move its value to this node.
    #         moveFromLeft(del_node.left, del_node)
    #     elif del_node.right: # Select the leftmost node on the right branch and move its value to this node.
    #         moveFromRight(del_node.right, del_node)
    #     else: # If no children, simply delete the node.
    #         del del_node

    #     return value

    # Generates an ordered list of all values in the tree.
    def orderedList(self):
        def rOrderedList(node_ptr, out_list):
            if node_ptr.left:
                rOrderedList(node_ptr.left, out_list)
            out_list.append(node_ptr.value)
            if node_ptr.right:
                rOrderedList(node_ptr.right, out_list)
            return

        out_list = []
        if self.root:
            rOrderedList(self.root, out_list)
        return out_list

    # Helper method for balanceTree()
    def _balancedTreeFromOrderedList(self, input_list):
        if len(input_list) == 1:
            return TreeNode(input_list[0])

        pivot = floor(len(input_list)/2)

        new_node = TreeNode(input_list[pivot])
        if pivot > 0:
            new_node.left = self._balancedTreeFromOrderedList(input_list[:pivot])
            new_node.left.parent = new_node
        if pivot < len(input_list)-1:
            new_node.right = self._balancedTreeFromOrderedList(input_list[pivot+1:])
            new_node.right.parent = new_node

        return new_node

    # Balances the tree so that its depth is no greater than log_2(N)
    def balanceTree(self):
        if not self.root: # Empty tree.
            return
        self.root = self._balancedTreeFromOrderedList(self.orderedList())

def findCommonAncestor(node1: TreeNode, node2: TreeNode):
    def getNodeDepth(cur_node):
        return 1 + getNodeDepth(cur_node.parent) if cur_node.parent else 1

    node1_depth = getNodeDepth(node1)
    node2_depth = getNodeDepth(node2)
    depth_delta = node1_depth - node2_depth

    node1_ptr, node2_ptr = node1, node2

    if depth_delta > 0: # Node 1 is deeper than Node 2.
        for i in range(0, depth_delta):
            node1_ptr = node1_ptr.parent
    else: # Node 2 is deeper or the same depth as Node 1.
        for i in range(0, -depth_delta):
            node2_ptr = node2_ptr.parent

    while node1_ptr:
        if node1_ptr == node2_ptr:
            return node1_ptr
        node1_ptr = node1_ptr.parent
        node2_ptr = node2_ptr.parent

    return None

# Balanced Binary tree nodes labelled 1 to 15.
t = BSTree(8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15)

print(findCommonAncestor(t.root.left.left.left, t.root.left.left.right))
print(findCommonAncestor(t.root.left.left.left, t.root.right.right.right))