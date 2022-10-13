/*
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
and deserialize(s), which deserializes the string back into the tree.
*/

class TreeNode {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }

    serialize() {
        function rSerialize(node, outStr) {
            if (node == null) {
                outStr = outStr.concat("\n");
            }
            else {
                outStr = outStr.concat(node.value, "\n");
                outStr = rSerialize(node.left, outStr);
                outStr = rSerialize(node.right, outStr);
            }
            return outStr;
        }
        
        return rSerialize(this, "");
    }
}

function deserialize(treeString){
    function rDeserialize(treeStringArr, index_ptr){
        if (treeStringArr[index_ptr[0]] == ""){
            index_ptr[0]++;
            return null;
        }
        else {
            const node = new TreeNode(treeStringArr[index_ptr[0]]);
            index_ptr[0]++;
            node.left = rDeserialize(treeStringArr, index_ptr);
            node.right = rDeserialize(treeStringArr, index_ptr);
            return node;
        }
    }

    const treeStringArr = treeString.split("\n");
    return rDeserialize(treeStringArr, [0]);
}

const root = new TreeNode("root");
root.left = new TreeNode("left");
root.left.left = new TreeNode("left.left");
root.right = new TreeNode("right");

const treeStr = root.serialize();
console.log(treeStr);
const dRoot = deserialize(treeStr);
console.assert(root.value == dRoot.value, "root mismatch");
console.assert(root.left.value == dRoot.left.value, "root.left mismatch");
console.assert(root.left.left.value == dRoot.left.left.value, "root.left.left mismatch"); 
console.assert(root.right.value == dRoot.right.value, "root.right mismatch");