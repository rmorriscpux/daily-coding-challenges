'''
In Ancient Greece, it was common to write text with the first line going left to right, the second line going right to left,
and continuing to go back and forth. This style was called “boustrophedon”.

Given a binary tree, write an algorithm to print the nodes in boustrophedon order.

For example, given the following tree:

       1
    /     \
  2         3
 / \       / \
4   5     6   7
You should return [1, 3, 2, 4, 5, 6, 7].
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
    
def boustrophedon(root: TreeNode):
    def rBoustrophedon(node: TreeNode, level: int, data_dict: dict):
        # Add data to data_dict at the current level.
        if level not in data_dict:
            data_dict[level] = []
        data_dict[level].append(node.data)
        # Recur left and right, going down one level.
        if node.left:
            rBoustrophedon(node.left, level+1, data_dict)
        if node.right:
            rBoustrophedon(node.right, level+1, data_dict)

        return
    
    data_dict = {}
    # Start recursion.
    rBoustrophedon(root, 0, data_dict)

    out_list = []
    for level in sorted(data_dict.keys()):
        # Extend forward on even levels, backward on odd levels.
        if level & 1:
            out_list.extend(data_dict[level][::-1])
        else:
            out_list.extend(data_dict[level])
    
    return out_list

t = TreeNode(1)
t.left = TreeNode(2)
t.left.left = TreeNode(4)
t.left.left.left = TreeNode(8)
t.left.left.right = TreeNode(9)
t.left.right = TreeNode(5)
t.left.right.left = TreeNode(10)
t.left.right.right = TreeNode(11)
t.right = TreeNode(3)
t.right.left = TreeNode(6)
t.right.left.left = TreeNode(12)
t.right.left.right = TreeNode(13)
t.right.right = TreeNode(7)
t.right.right.left = TreeNode(14)
t.right.right.right = TreeNode(15)

print(boustrophedon(t))