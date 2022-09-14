'''
Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

    a
   / \
  b   c
 /
d
'''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def deepestNode(root: TreeNode):
    def rDeepestNode(cur_node, depth):
        left_node, left_depth = None, None
        right_node, right_depth = None, None
        if cur_node.left:
            left_node, left_depth = rDeepestNode(cur_node.left, depth+1)
        if cur_node.right:
            right_node, right_depth = rDeepestNode(cur_node.right, depth+1)

        if not left_node and not right_node:
            return cur_node, depth
        elif left_node and not right_node:
            return left_node, left_depth
        elif not left_node and right_node:
            return right_node, right_depth
        else:
            if left_depth >= right_depth:
                return left_node, left_depth
            else:
                return right_node, right_depth

    node, depth = rDeepestNode(root, 0)
    return node

root = TreeNode('a')
root.left = TreeNode('b')
root.left.left = TreeNode('c')
root.left.left.right = TreeNode('d')
root.right = TreeNode('e')
root.right.left = TreeNode('f')
root.right.right = TreeNode('g')

print(deepestNode(root).value)