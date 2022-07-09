'''
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Convert a binary tree to a string. Using line breaks as the separator in this case. Left-to-right traversal.
def serialize(root):
    def rSerialize(node, out_str):
        if node == None:
            out_str += "\n"
        else:
            out_str += str(node.val) + "\n"
            out_str = rSerialize(node.left, out_str)
            out_str = rSerialize(node.right, out_str)
        return out_str

    return rSerialize(root, "")

# Convert a serialized string to a binary tree.
def deserialize(s):
    # In Python, integers passed by value while lists are passed by reference. So for this recursion, the index is represented as a list of one integer so it can be modified within the recursion.
    def rDeserialize(str_arr, index):
        if str_arr[index[0]] == "":
            index[0] += 1
            return None
        else:
            child_node = Node(str_arr[index[0]])
            index[0] += 1
            child_node.left = rDeserialize(str_arr, index)
            child_node.right = rDeserialize(str_arr, index)
            return child_node

    # Methodology is to split the string for simplicity of the recursive subroutine.
    index = [0]
    str_arr = s.split("\n")
    return rDeserialize(str_arr, index)

tree = Node("root", Node("left", Node("left.left")), Node("right"))
print(serialize(tree))
assert deserialize(serialize(tree)).left.left.val == "left.left"
assert deserialize(serialize(tree)).right.val == "right"