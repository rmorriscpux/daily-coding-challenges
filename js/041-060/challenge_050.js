/*
Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '-', '*', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5

You should return 45, as it is (3 + 2) * (4 + 5).
*/

class TreeNode {
    constructor(val) {
        // Data entry check: val must be a number or an operator.
        if ((typeof val != "number") && !(['+', '-', '*', '/'].includes(val))) {
            throw TypeError;
        }
        if (val == NaN) {
            throw RangeError;
        }

        this.val = val;
        this.left = null;
        this.right = null;
    }

    toString() {
        let outStr = this.val.toString();
        if (this.left != null) {
            outStr += ", [left: " + this.left.toString() + "]";
        }
        if (this.right != null) {
            outStr += ", [right: " + this.right.toString() + "]";
        }
        return outStr;
    }
}

function solveBinaryTree(treeNode) {
    if (!['+', '-', '*', '/'].includes(treeNode.val)) {
        throw TypeError;
    }

    let leftResult = 0;
    if (treeNode.left) {
        if (typeof treeNode.left.val == "number") {
            leftResult = treeNode.left.val;
        }
        else {
            leftResult = solveBinaryTree(treeNode.left);
        }
    }

    let rightResult = 0;
    if (treeNode.right) {
        if (typeof treeNode.right.val == "number") {
            rightResult = treeNode.right.val;
        }
        else {
            rightResult = solveBinaryTree(treeNode.right);
        }
    }

    let result = NaN;
    switch (treeNode.val) {
        case '+':
            result = leftResult + rightResult;
            break;
        case '-':
            result = leftResult - rightResult;
            break;
        case '*':
            result = leftResult * rightResult;
            break;
        case '/':
            result = leftResult / rightResult;
            break;
        default:
            throw SyntaxError;
    }

    return result;
}

const t1 = new TreeNode('*');
t1.left = new TreeNode('+');
t1.right = new TreeNode('+');
t1.left.left = new TreeNode(3);
t1.left.right = new TreeNode(2);
t1.right.left = new TreeNode(4);
t1.right.right = new TreeNode(5);

const t2 = new TreeNode('*');
t2.left = new TreeNode('+');
t2.right = new TreeNode('-');
t2.left.left = new TreeNode(3);
t2.left.right = new TreeNode(2);
t2.right.left = new TreeNode(4);
t2.right.right = new TreeNode(5);

console.log(solveBinaryTree(t1));
console.log(solveBinaryTree(t2));