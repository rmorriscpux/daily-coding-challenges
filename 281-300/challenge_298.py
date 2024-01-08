'''
A girl is walking along an apple orchard with a bag in each hand. She likes to pick apples from each tree as she goes along,
but is meticulous about not putting different kinds of apples in the same bag.

Given an input describing the types of apples she will pass on her path, in order,
determine the length of the longest portion of her path that consists of just two types of apple trees.

For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], the longest portion will involve types 1 and 3, with a length of four.
'''

class TreeCount:
    def __init__(self, type: int):
        self.type = type
        self.counter = 1

    def __repr__(self):
        return f"TreeCount({self.type}: {self.counter})"

def twoAppleTypes(orchard: list[int]) -> int:
    max_length = 0
    cur_length = 0

    cur_portion = []

    for tree in orchard:
        if len(cur_portion) == 0:
            cur_portion.insert(0, TreeCount(tree))
            cur_length = 1
        elif len(cur_portion) == 1:
            if cur_portion[0].type == tree:
                cur_portion[0].counter += 1
            else:
                cur_portion.insert(0, TreeCount(tree))
            cur_length += 1
        else:
            if cur_portion[0].type == tree:
                cur_portion[0].counter += 1
            elif cur_portion[1].type == tree:
                temp_tree = cur_portion.pop()
                temp_tree.counter += 1
                cur_portion.insert(0, temp_tree)
            else:
                cur_portion.pop()
                cur_portion.insert(0, TreeCount(tree))
            cur_length = cur_portion[0].counter + cur_portion[1].counter
            
        if cur_length > max_length:
            max_length = cur_length
    
    return max_length

if __name__ == "__main__":
    print(twoAppleTypes([2, 1, 2, 3, 3, 1, 3, 5]))