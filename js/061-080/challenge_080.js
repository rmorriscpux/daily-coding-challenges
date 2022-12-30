/*
Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

    a
   / \
  b   c
 /
d
*/

class TreeNode {
    constructor(data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

function deepestNode(treeRoot) {
    function rDeepestNode(node, depth) {
        // Has left and right children.
        if (node.left != null && node.right != null) {
            const leftResult = rDeepestNode(node.left, depth+1);
            const rightResult = rDeepestNode(node.right, depth+1);
            return leftResult.depth >= rightResult.depth ? leftResult : rightResult;
        }
        // Only has left child.
        if (node.left != null) {
            return rDeepestNode(node.left, depth+1);
        }
        // Only has right child.
        if (node.right != null) {
            return rDeepestNode(node.right, depth+1);
        }
        // Neither left nor right.
        return {'node' : node, 'depth' : depth};
    }

    const result = rDeepestNode(treeRoot, 0);
    return result.node;
}

//     a
//    / \
//   b   e
//  /   / \
// c   f   g
//  \
//   d

const root = new TreeNode('a');
root.left = new TreeNode('b');
root.left.left = new TreeNode('c');
root.left.left.right = new TreeNode('d');
root.right = new TreeNode('e');
root.right.left = new TreeNode('f');
root.right.right = new TreeNode('g');

console.log(deepestNode(root));