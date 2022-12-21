/*
Given an undirected graph represented as an adjacency matrix and an integer k, write a function to determine
whether each vertex in the graph can be colored such that no two adjacent vertices share the same color using at most k colors.
*/

// Adjacency Matrix - A matrix representing vertices in a finite graph.

function coloredVertices(graph, k) {
    function rColoredVertices(graph, k, colors) {
        // End Case.
        if (colors.length == graph.length) {
            return true;
        }

        for (let i = 0; i < k; i++) {
            colors.push(i);
            let lastVertex = colors.length - 1;
            const coloredNeighbors = [];
            let colorsValid = true;
            // Check that there's still a color available not taken up by any neighbors.
            for (let j = 0; j < graph[lastVertex].length; j++) {
                if (graph[lastVertex][j] != 0 && j < lastVertex) {
                    coloredNeighbors.push(j);
                }
            }
            for (let j = 0; j < coloredNeighbors.length; j++) {
                if (colors[coloredNeighbors[j]] == colors[colors.length-1]) {
                    // Adjacent matching colors.
                    colorsValid = false;
                    break;
                }
            }

            // Recur if colors are valid, return true if it's all good.
            if (colorsValid && rColoredVertices(graph, k, colors)) {
                return true;
            }

            colors.pop();
        }

        return false;
    }

    return rColoredVertices(graph, k, []);
}

const aMatrix = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
];

console.log(coloredVertices(aMatrix, 2));
console.log(coloredVertices(aMatrix, 3));
console.log(coloredVertices(aMatrix, 4));