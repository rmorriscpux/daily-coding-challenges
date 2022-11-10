'''
Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

  10
 /  \
5    5
 \     \
   2    1
       /
     -1
'''

class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"TreeNode({self.value})"

def minPathSum(root: TreeNode):
    def rMinPathSum(node, cur_sum):
        if node.left and node.right:
            return min(rMinPathSum(node.left, cur_sum + node.value), rMinPathSum(node.right, cur_sum + node.value))
        elif node.left:
            return rMinPathSum(node.left, cur_sum + node.value)
        elif node.right:
            return rMinPathSum(node.right, cur_sum + node.value)
        else:
            return cur_sum + node.value

    return rMinPathSum(root, 0)

root = TreeNode(10)
root.left = TreeNode(5)
root.left.right = TreeNode(2)
root.right = TreeNode(5)
root.right.right = TreeNode(1)
root.right.right.left = TreeNode(-1)

print(minPathSum(root))