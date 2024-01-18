'''
Given a binary search tree, find the floor and ceiling of a given integer. The floor is the highest element in the tree
less than or equal to an integer, while the ceiling is the lowest element in the tree greater than or equal to an integer.

If either value does not exist, return None.
'''

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    @staticmethod
    def fromList(num_list: list[int]):
        def rFromList(sub_list: list[int]):
            if len(sub_list) == 0:
                return None
            if len(sub_list) == 1:
                return BSTNode(sub_list[0])
            
            pivot = len(sub_list) // 2

            new_node = BSTNode(sub_list[pivot])
            new_node.left = rFromList(sub_list[:pivot])
            new_node.right = rFromList(sub_list[pivot+1:])

            return new_node
        
        new_bst = BST()
        new_bst.root = rFromList(sorted(num_list))
        
        return new_bst
    
    def addValue(self, value: int):
        def rAddValue(node: BSTNode, value: int):
            if value < node.value:
                if node.left:
                    rAddValue(node.left, value)
                else:
                    node.left = BSTNode(value)
            elif value > node.value:
                if node.right:
                    rAddValue(node.right, value)
                else:
                    node.right = BSTNode(value)
            return

        if not self.root:
            self.root = BSTNode(value)
            return self
        
        rAddValue(self.root, value)

        return self
    
    def floorAndCeil(self, target: int):
        def rFloorAndCeil(node: BSTNode, target: int, f_c: list):
            if node.value < target:
                if f_c[0] is None or f_c[0] < node.value:
                    f_c[0] = node.value
                if node.right:
                    rFloorAndCeil(node.right, target, f_c)
            elif node.value > target:
                if f_c[1] is None or f_c[1] > node.value:
                    f_c[1] = node.value
                if node.left:
                    rFloorAndCeil(node.left, target, f_c)
            else:
                f_c[0] = target
                f_c[1] = target
            return

        if not self.root:
            return [None, None]

        target_floor_and_ceil = [None, None]

        rFloorAndCeil(self.root, target, target_floor_and_ceil)

        return target_floor_and_ceil

if __name__ == "__main__":
    bst = BST.fromList(list(range(0, 30, 2)))

    print(bst.floorAndCeil(15)) # [14, 16]
    print(bst.floorAndCeil(3)) # [2, 4]
    print(bst.floorAndCeil(8)) # [8, 8]
    print(bst.floorAndCeil(100)) # [28, None]
    print(bst.floorAndCeil(-3)) # [None, 0]
    print(BST().floorAndCeil(1)) # [None, None] (Empty BST)