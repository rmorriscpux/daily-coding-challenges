'''
Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f

should become:

  a
 / \
 c  b
 \  / \
  f e  d
'''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def invertTree(node: TreeNode):
    temp = node.left
    node.left = node.right
    node.right = temp
    del temp # For space optimization.

    if node.left:
        invertTree(node.left)

    if node.right:
        invertTree(node.right)

    return

if __name__ == "__main__":
    print("Testing invertTree()")

    root = TreeNode('a')
    root.left = TreeNode('b')
    root.right = TreeNode('c')
    root.left.left = TreeNode('d')
    root.left.right = TreeNode('e')
    root.right.left = TreeNode('f')

    assert (root.value == 'a' and
        root.left.value == 'b' and
        root.right.value == 'c' and
        root.left.left.value == 'd' and
        root.left.right.value == 'e' and
        root.right.left.value == 'f')

    invertTree(root)

    assert (root.value == 'a' and
        root.right.value == 'b' and
        root.left.value == 'c' and
        root.right.right.value == 'd' and
        root.right.left.value == 'e' and
        root.left.right.value == 'f')

    print("Done!")