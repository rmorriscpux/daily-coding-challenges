'''
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string 'de' and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
'''

# Tree Node Class
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_node(self, new_node_data):
        if new_node_data < self.data:
            if self.left == None:
                self.left = TreeNode(new_node_data)
            else:
                self.left.insert_node(new_node_data)
        else:
            if self.right == None:
                self.right = TreeNode(new_node_data)
            else:
                self.right.insert_node(new_node_data)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()


def autocomplete(s, query_set):
    # query_set to Binary Search Tree
    bst = TreeNode(query_set[0])
    for i in range(1, len(query_set)):
        bst.insert_node(query_set[i])

    # bst.print_tree()

    # Conduct Search.
    def search_string(s, tree_node):
        result = []
        if s == tree_node.data[:len(s)]:
            result.append(tree_node.data)

        if tree_node.left is not None:
            if s <= tree_node.data[:len(s)]:
                result = search_string(s, tree_node.left) + result

        if tree_node.right is not None:
            if s >= tree_node.data[:len(s)]:
                result = result + search_string(s, tree_node.right)

        return result

    return search_string(s, bst)

WORD_LIST = [
    "mistreat",
    "admission",
    "smell",
    "prestige",
    "electronics",
    "gene",
    "emergency",
    "assessment",
    "herb",
    "amber",
    "lane",
    "teach",
    "organ",
    "blackmail",
    "decay",
    "valley",
    "miserable",
    "active",
    "occasion",
    "heaven",
    "wheat",
    "hilarious",
    "host",
    "sail",
    "multimedia",
    "muggy",
    "evaluate",
    "coal",
    "snack",
    "pain",
    "conservation",
    "deteriorate",
    "rent",
    "gradual",
    "proclaim",
    "ecstasy",
    "mind",
    "shed",
    "reverse",
    "talented",
    "modest",
    "sickness",
    "capital",
    "tell",
    "dentist",
    "generation",
    "rescue",
    "sensation",
    "fund",
    "joke",
]

print(autocomplete("g", WORD_LIST))