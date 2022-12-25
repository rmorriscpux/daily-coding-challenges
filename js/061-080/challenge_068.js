/*
On our special chessboard, two bishops attack each other if they share the same diagonal.
This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M chessboard.
Write a function to count the number of pairs of bishops that attack each other.
The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).

For example, given M = 5 and the list of bishops:

(0, 0)
(1, 2)
(2, 2)
(4, 0)

The board would look like this:

[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]

You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.
*/

// Include hash function.
const { createHash } = require('crypto');

function bishopAttacks(bishops, M) {
    if (typeof(M) != 'number') throw TypeError("M must be number.");
    if (M <= 0) throw RangeError("M must be positive.");

    // Helper function to convert two coordinates into a hash digest string. This is necessary to identify coordinate pairs in a set.
    const hash = (coords) => createHash('sha256').update(coords[0].toString()).update(coords[1].toString()).digest('hex');

    let count = 0;
    const attackablePositions = [];

    for (currentBishop of bishops) {
        if (currentBishop[0] < 0 || currentBishop[0] >= M ||
            currentBishop[1] < 0 || currentBishop[1] >= M) {
                throw RangeError("Bishop out of bounds. Bishop=[%d, %d], M=%d", currentBishop[0], currentBishop[1], M);
            }

        // Determine if the current bishop is under threat from any previously placed bishops.
        // Note that the count is for the number of pairs of bishops that threaten each other, so we only count once.
        // Also that the current bishop can be under threat from more than one previously placed bishop.
        let bishopHash = hash(currentBishop);
        for (bishopThreat of attackablePositions) {
            if (bishopThreat.has(bishopHash)) {
                count++;
            }
        }

        // Create set of positions where the bishop can move.
        let movablePositions = new Set();

        // Northwest
        let i = currentBishop[0]-1, j = currentBishop[1]-1;
        while (i >= 0 && j >= 0) {
            movablePositions.add(hash([i, j]));
            i--;
            j--;
        }

        // Northeast
        i = currentBishop[0]+1, j = currentBishop[1]-1;
        while (i < M && j >= 0) {
            movablePositions.add(hash([i, j]));
            i++;
            j--;
        }

        // Southeast
        i = currentBishop[0]+1, j = currentBishop[1]+1;
        while (i < M && j < M) {
            movablePositions.add(hash([i, j]));
            i++;
            j++;
        }

        // Southwest
        i = currentBishop[0]-1, j = currentBishop[1]+1;
        while (i >= 0 && j < M) {
            movablePositions.add(hash([i, j]));
            i--;
            j++;
        }

        // Add this set to the list containing each bishop's attackable positions.
        attackablePositions.push(movablePositions);
    }

    return count;
}

console.log(bishopAttacks([[0, 0], [1, 2], [2, 2], [4, 0]], 5));