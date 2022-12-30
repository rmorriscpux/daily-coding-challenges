/*
In a directed graph, each node is assigned an uppercase letter.
We define a path's value as the number of most frequently-occurring letter along that path.
For example, if a path in the graph goes through "ABACA", the value of the path is 3, since there are 3 occurrences of 'A' on the path.

Given a graph with n nodes and m directed edges, return the largest value path of the graph.
If the largest value is infinite, then return null.

The graph is represented with a string and an edge list.
The i-th character represents the uppercase letter of the i-th node.
Each tuple in the edge list (i, j) means there is a directed edge from the i-th node to the j-th node.
Self-edges are possible, as well as multi-edges.

For example, the following input graph:

ABACA

[(0, 1),
 (0, 2),
 (2, 3),
 (3, 4)]

Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).

The following input graph:

A

[(0, 0)]

Should return null, since we have an infinite loop.
*/

function getPathValue(pathString, edges) {
    // Deep copy shortcut.
    const deepcopy = (o) => JSON.parse(JSON.stringify(o));

    function rGetPathValue(graphPath, node, adjacencies) {
        if (graphPath['nodes'].includes(node)) {
            return [graphPath];
        }

        const newGraphPath = deepcopy(graphPath);
        newGraphPath['nodes'].push(node);
        if (!newGraphPath['letterCounts'].hasOwnProperty(node.charAt(0))) {
            newGraphPath['letterCounts'][node.charAt(0)] = 0;
        }
        newGraphPath['letterCounts'][node.charAt(0)]++;

        if (!adjacencies.hasOwnProperty(node)) {
            return [newGraphPath];
        }

        const paths = [];
        let newPaths = [];

        for (subNode of adjacencies[node]) {
            newPaths = rGetPathValue(newGraphPath, subNode, adjacencies);
            paths.push(...newPaths);
        }

        return paths;
    }

    // Build a list of nodes with unique IDs from the path string.
    const letters = [];
    const nodeCounts = {};
    for (let i = 0; i < pathString.length; i++) {
        let letter = pathString.charAt(i);
        if (!nodeCounts.hasOwnProperty(letter)) {
            nodeCounts[letter] = 0;
        }
        letters.push(letter.concat(nodeCounts[letter].toString()));
        nodeCounts[letter]++;
    }

    // Tie the path-node list to adjacencies based on the edges. Omit self-edges.
    const adjacencies = {};
    for (let edge of edges) {
        let start = edge[0], end = edge[1];
        if (!adjacencies.hasOwnProperty(letters[start])) {
            adjacencies[letters[start]] = new Set();
        }
        if (start != end) {
            adjacencies[letters[start]].add(letters[end]);
        }
    }

    // Build a list of dictionaries containing the possible paths, using the recursive subroutine.
    const paths = [];
    let newPaths = [];
    for (let node of Object.keys(adjacencies)) {
        newPaths = rGetPathValue({'nodes': [], 'letterCounts': {}}, node, adjacencies);
        paths.push(...newPaths);
    }

    // Get the maximum path value.
    let maxValue = 0;
    for (let path of paths) {
        for (let key of Object.keys(path['letterCounts'])) {
            maxValue = path.letterCounts[key] > maxValue ? path.letterCounts[key] : maxValue;
        }
    }

    return maxValue > 0 ? maxValue : null;
}

console.log(getPathValue("ABACA", [[0, 1], [0, 2], [2, 3], [3, 4]]));