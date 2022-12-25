/*
There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of
starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

    Right, then down
    Down, then right

Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
*/

// Note: Board contents are irrelevant. Only the dimensions are needed.

const assert = require('assert');

function countTraversals(matrix) {
    function rCountTraversals(x, y, M, N) {
        // End case: At bottom right.
        if (x == M-1 && y == N-1) {
            return 1;
        }

        let count = 0;
        // Can go right.
        if (x < M-1) {
            count += rCountTraversals(x+1, y, M, N);
        }
        // Can go down.
        if (y < N-1) {
            count += rCountTraversals(x, y+1, M, N);
        }

        return count;
    }

    // Setup
    for (let i = 1; i < matrix.length; i++) {
        assert(matrix[i].length == matrix[0].length);
    }

    return rCountTraversals(0, 0, matrix[0].length, matrix.length);
}

const m1 = [
    [0, 0],
    [0, 0]
];

const m2 = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
];

console.log(countTraversals(m1));
console.log(countTraversals(m2));