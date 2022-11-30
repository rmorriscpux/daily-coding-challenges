/*
Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g
*/

class TreeNode {
    constructor(data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }

    toString() {
        let outStr = this.data.toString();
        if (this.left != null) {
            outStr += ", [left: " + this.left.toString() + "]";
        }
        if (this.right != null) {
            outStr += ", [right: " + this.right.toString() + "]";
        }
        return outStr;
    }

    printTreeInOrder() {
        function getTreeInOrder(node, treeArr) {
            if (node.left != null) {
                getTreeInOrder(node.left, treeArr);
            }
            treeArr.push(node.data);
            if (node.right != null) {
                getTreeInOrder(node.right, treeArr);
            }

            return treeArr;
        }

        console.log(getTreeInOrder(this, []));
        return;
    }

    printTreePreOrder() {
        function getTreePreOrder(node, treeArr) {
            treeArr.push(node.data);
            if (node.left != null) {
                getTreePreOrder(node.left, treeArr);
            }
            if (node.right != null) {
                getTreePreOrder(node.right, treeArr);
            }

            return treeArr;
        }

        console.log(getTreePreOrder(this, []));
        return;
    }
}

function buildTree(preOrder, inOrder) {
    if (!(preOrder && inOrder)) {
        return null;
    }

    let root = new TreeNode(preOrder[0]);

    if (preOrder.length == 1) {
        return root;
    }

    for (i = 0; i < inOrder.length; i++) {
        if (inOrder[i] == root.data) {
            root.left = buildTree(preOrder.slice(1, i+1), inOrder.slice(0, i));
            root.right = buildTree(preOrder.slice(i+1), inOrder.slice(i+1));
        }
    }

    return root;
}

const tree = buildTree(['a', 'b', 'd', 'e', 'c', 'f', 'g'], ['d', 'b', 'e', 'a', 'f', 'c', 'g']);
console.log(tree.toString());
tree.printTreePreOrder();
tree.printTreeInOrder();