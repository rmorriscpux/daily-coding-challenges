'''
Given a sorted array, convert it into a height-balanced binary search tree.
'''

import sys

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        out_str = f"{self.data}"
        if self.left or self.right:
            out_str = out_str + "->["
            if self.left:
                out_str = out_str + f"L: {self.left}"
            if self.left and self.right:
                out_str = out_str + " | "
            if self.right:
                out_str = out_str + f"R: {self.right}"
            out_str = out_str + "]"
        return out_str

class BST:
    def __init__(self, root: BSTNode=None):
        self.root = root

    def __str__(self):
        return "BST(" + str(self.root) + ")"

    # Relevant Method. Assumes list is pre-sorted. Static method is called without instantiating the class.
    @staticmethod
    def fromSortedList(l: list):
        def rFromSortedList(sub_l: list):
            # Cases for when list length is 0 or 1.
            if not sub_l:
                return None
            if len(sub_l) == 1:
                return BSTNode(sub_l[0])
            # Split list down the middle. Create new node from the pivot item,
            # with the branches being the left and right sides of the rest of the list.
            pivot = len(sub_l) // 2

            new_node = BSTNode(sub_l[pivot])
            new_node.left = rFromSortedList(sub_l[:pivot])
            new_node.right = rFromSortedList(sub_l[pivot+1:])

            return new_node
        
        new_bst = BST()
        new_bst.root = rFromSortedList(l)
        return new_bst
    
    # Print the min and max depth of the tree. In a balanced tree, the min and max depths must differ by 0 or 1.
    def testMinAndMaxDepth(self):
        def rTestMinAndMaxDepth(node: BSTNode, depths: dict[str, int], cur_depth: int=1):
            if not (node.left or node.right):
                depths["min"] = min(depths["min"], cur_depth)
                depths["max"] = max(depths["max"], cur_depth)
                return
            if node.left:
                rTestMinAndMaxDepth(node.left, depths, cur_depth+1)
            if node.right:
                rTestMinAndMaxDepth(node.right, depths, cur_depth+1)
            return
        
        depths = {
            "min" : sys.maxsize,
            "max" : 1
        }
        rTestMinAndMaxDepth(self.root, depths)

        print(f"Min Depth: {depths["min"]} | Max Depth: {depths["max"]}")

        return
    
if __name__ == "__main__":
    tree = BST.fromSortedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(tree)
    tree.testMinAndMaxDepth()
    tree2 = BST.fromSortedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    print(tree2)
    tree2.testMinAndMaxDepth()