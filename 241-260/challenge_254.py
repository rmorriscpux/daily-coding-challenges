'''
Recall that a full binary tree is one in which each node is either a leaf node, or has two children.
Given a binary tree, convert it to a full one by removing nodes with only one child.

For example, given the following tree:

         0
      /     \
    1         2
  /            \
3                 4
  \             /   \
    5          6     7
You should convert it to:

     0
  /     \
5         4
        /   \
       6     7
'''

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        pr_left = f" | left: {self.left}" if self.left else ""
        pr_right = f" | right: {self.right}" if self.right else ""
        return f"TreeNode({self.data}" + pr_left + pr_right + ")"
    
def fullBinaryTree(root: TreeNode):
    def rFullBinaryTree(node: TreeNode):
        if node.left and node.right:
            node.left = rFullBinaryTree(node.left)
            node.right = rFullBinaryTree(node.right)
            return node

        if not (node.left or node.right):
            return node
        
        if node.left:
            return rFullBinaryTree(node.left)
        if node.right:
            return rFullBinaryTree(node.right)
        
    root = rFullBinaryTree(root)
    return
    
root = TreeNode(0)
root.left = TreeNode(1)
root.left.left = TreeNode(3)
root.left.left.right = TreeNode(5)
root.right = TreeNode(2)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(6)
root.right.right.right = TreeNode(7)

print(root)
fullBinaryTree(root)
print(root)