'''
Given a node in a binary tree, return the next bigger element, also known as the inorder successor. 

For example, the inorder successor of 22 is 30.

   10
  /  \
 5    30
     /  \
   22    35

You can assume each node has a parent pointer.
'''

class BSTNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return f"BSTNode({self.value})"

class BST:
    def __init__(self, *values: int):
        self.root = None
        for v in values:
            self.addNode(v)

    def addNode(self, value: int):
        def rAddNode(cur_node, value):
            if value < cur_node.value:
                if cur_node.left:
                    rAddNode(cur_node.left, value)
                else:
                    cur_node.left = BSTNode(value)
                    cur_node.left.parent = cur_node
            elif value > cur_node.value:
                if cur_node.right:
                    rAddNode(cur_node.right, value)
                else:
                    cur_node.right = BSTNode(value)
                    cur_node.right.parent = cur_node
            return

        if self.root:
            rAddNode(self.root, value)
        else:
            self.root = BSTNode(value)

        return self

def getInorderSuccessor(node: BSTNode):
    out_node = None
    # First candidate: The leftmost descendant of the right side of the node.
    if node.right:
        cur_node = node.right
        while cur_node.left:
            cur_node = cur_node.left
        out_node = cur_node
    # Second candidate: The first ancestor that's greater than the child it's coming from. (i.e. the child is the left child of the parent)
    elif node.parent:
        cur_node = node
        while cur_node.parent:
            if cur_node.value < cur_node.parent.value:
                out_node = cur_node.parent
                break
            cur_node = cur_node.parent

    return out_node

bst = BST(8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15)

n1 = bst.root.left # 4
n2 = bst.root.right.left # 10
n3 = bst.root # 8
n4 = bst.root.right.right.right # 15

print(getInorderSuccessor(n1), getInorderSuccessor(n2), getInorderSuccessor(n3), getInorderSuccessor(n4))