/*
A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N chessboard.
*/

// Include hash function.
const { createHash } = require('crypto');

// Add union function to Set type as Javascript ES6 does not have this built in. Returns a new Set instead of adding to the existing Set.
Set.prototype.union = function(otherSet) {
    if (!otherSet instanceof Set) throw TypeError("Parameter must be a Set");
    
    const unionSet = new Set(this.values());
    otherSet.forEach((v) => unionSet.add(v));

    return unionSet;
}

function countKnightsTours(N) {
    if (!(typeof(N) == 'number')) throw TypeError("Parameter must be a number");

    // Helper function to convert two coordinates into a hash digest string. This is necessary to identify coordinate pairs in a set.
    const hash = (coords) => createHash('sha256').update(coords[0].toString()).update(coords[1].toString()).digest('hex');

    function rCountKnightsTours(N, curPos, visitedPos) {
        // Completed tour: All positions visited.
        if (visitedPos.size == N * N) {
            return 1;
        }

        // The knight moves 1 position straight then 1 position diagonal on a chess board.
        const KNIGHT_MOVES = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [2, -1], [2, 1], [1, -2], [1, 2]];
        // Now build a list of possible moves on the board, omitting any positions the knight already visited.
        const validMoves = [];
        for (move of KNIGHT_MOVES) {
            let newX = curPos[0] + move[0], newY = curPos[1] + move[1];
            // Valid if new X and new Y are on the board, and the position was not already visited.
            if (newX >= 0 && newX < N && newY >= 0 && newY < N && !visitedPos.has(hash([newX, newY]))) {
                validMoves.push([newX, newY]);
            }
        }

        // Now get the count by recurring into the routine adding each valid move.
        let count = 0;
        for (nextPos of validMoves) {
            count += rCountKnightsTours(N, nextPos, visitedPos.union(new Set([hash(nextPos)])));
        }

        return count;
    }

    if (N <= 0) return 0;

    let count = 0;
    for (let x = 0; x < N; x++) {
        for (let y = 0; y < N; y++) {
            count += rCountKnightsTours(N, [x, y], new Set([hash([x, y])]));
        }
    }

    return count;
}

// Note: This gets very time intensive. O((N^2)!)
console.log(countKnightsTours(1));
console.log(countKnightsTours(2));
console.log(countKnightsTours(3));
console.log(countKnightsTours(4));
console.log(countKnightsTours(5));