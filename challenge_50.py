'''
Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5

You should return 45, as it is (3 + 2) * (4 + 5).
'''

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def solveBinaryTree(root: TreeNode):
    assert root.data in ['+', '-', '*', '/']

    if root.left.data in ['+', '-', '*', '/']:
        left_result = solveBinaryTree(root.left)
    else:
        left_result = root.left.data

    if root.right.data in ['+', '-', '*', '/']:
        right_result = solveBinaryTree(root.right)
    else:
        right_result = root.right.data


    if root.data == '+':
        result = left_result + right_result
    elif root.data == '-':
        result = left_result - right_result
    elif root.data == '*':
        result = left_result * right_result
    elif root.data == '/':
        result = left_result / right_result

    return result

t1 = TreeNode('*')
t1.left = TreeNode('+')
t1.right = TreeNode('+')
t1.left.left = TreeNode(3)
t1.left.right = TreeNode(2)
t1.right.left = TreeNode(4)
t1.right.right = TreeNode(5)

t2 = TreeNode('*')
t2.left = TreeNode('+')
t2.right = TreeNode('-')
t2.left.left = TreeNode(3)
t2.left.right = TreeNode(2)
t2.right.left = TreeNode(4)
t2.right.right = TreeNode(5)

print(solveBinaryTree(t1))
print(solveBinaryTree(t2))