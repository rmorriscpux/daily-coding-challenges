'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s.
A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
'''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def buildTree(root_value, *node_values):
    def addNode(val, root: TreeNode):
        if val < root.value:
            if root.left:
                addNode(val, root.left)
            else:
                root.left = TreeNode(val)
        else:
            if root.right:
                addNode(val, root.right)
            else:
                root.right = TreeNode(val)
        return

    root = TreeNode(root_value)
    for value in node_values:
        addNode(value, root)

    return root

# Function Problem
def detectSubtree(s: TreeNode, t: TreeNode):
    # Subroutine to directly compare two tree roots.
    def treeCompare(t1, t2):
        if t1.value != t2.value:
            return False

        # Ensure the child profiles match.
        if (t1.left and not t2.left) or (t2.left and not t1.left) or (t1.right and not t2.right) or (t2.right and not t1.right):
            return False

        equivalent = True
        if t1.left:
            equivalent = equivalent and treeCompare(t1.left, t2.left)
        if t1.right and equivalent:
            equivalent = equivalent and treeCompare(t1.right, t2.right)

        return equivalent

    if not s or not t:
        return False

    # Compare the tree roots. If not equivalent, compare s to the roots for the left and right branches of t.
    if treeCompare(s, t):
        return True

    return detectSubtree(s.left, t) or detectSubtree(s.right, t)

tree1 = buildTree(8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15)
tree2 = buildTree(4, 2, 1, 3, 6, 5, 7)
tree3 = buildTree(12, 10, 9, 11, 14, 13, 16)
tree4 = buildTree(4, 2, 1, 3, 6, 5)

print(detectSubtree(tree1, tree2)) # True
print(detectSubtree(tree1, tree3)) # False
print(detectSubtree(tree1, tree4)) # False
print(detectSubtree(tree1, tree1)) # True