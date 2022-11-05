/*
You are given an M by N matrix consisting of booleans that represents a board.
Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps
required to reach the end coordinate from the start. If there is no possible path, then return null.
You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]

and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7,
since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
*/

function shortestPath(board, start, end) {
    function validMove(board, traversed, x, y){
        return ((x >= 0 && x < board[0].length) &&
            (y >= 0 && y < board.length) &&
            !board[y][x] && !traversed[y][x]);
    }

    function rShortestPath(board, traversed, x, y, endX, endY, minDistance, curDistance) {
        if (x == endX && y == endY) {
            minDistance[0] = curDistance < minDistance[0] ? curDistance : minDistance[0];
            return;
        }

        traversed[y][x] = true;
        // Up
        if (validMove(board, traversed, x, y-1)){
            rShortestPath(board, traversed, x, y-1, endX, endY, minDistance, curDistance+1);
        }
        // Down
        if (validMove(board, traversed, x, y+1)){
            rShortestPath(board, traversed, x, y+1, endX, endY, minDistance, curDistance+1);
        }
        // Left
        if (validMove(board, traversed, x-1, y)){
            rShortestPath(board, traversed, x-1, y, endX, endY, minDistance, curDistance+1);
        }
        // Right
        if (validMove(board, traversed, x+1, y)){
            rShortestPath(board, traversed, x+1, y, endX, endY, minDistance, curDistance+1);
        }

        traversed[y][x] = false;
        return
    }

    const traversed = board.map(row=>row.map(()=>false)); // Makes traversed a 2D array of "false" the same dimensions as board.

    const distance = [Number.POSITIVE_INFINITY];

    rShortestPath(board, traversed, start[0], start[1], end[0], end[1], distance, 0);

    return distance[0] < Number.POSITIVE_INFINITY ? distance[0] : null;
}

const board = [
    [false, false, false, false],
    [true, true, false, true],
    [false, false, false, false],
    [false, false, false, false],
];

console.log(shortestPath(board, [0, 3], [0, 0]));