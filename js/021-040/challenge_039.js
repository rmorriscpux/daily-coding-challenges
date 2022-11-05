/*
Conway's Game of Life takes place on an infinite two-dimensional board of square cells.
Each cell is either dead or alive, and at each tick, the following rules apply:

    Any live cell with less than two live neighbours dies.
    Any live cell with two or three live neighbours remains living.
    Any live cell with more than three live neighbours dies.
    Any dead cell with exactly three live neighbours becomes a live cell.

A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life.
It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for.
Once initialized, it should print out the board state at each step.
Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
*/

function gameOfLife(coords, steps) {
    function printBoard(board, grid) {
        let outStr = " |";
        for (let i = grid['minX']; i < grid['maxX']; i++) {
            outStr += i.toString();
        }
        outStr += "\n";
        outStr += "-".repeat(grid[maxX] - grid[minX] + 2) + "\n";
        for (let i = grid['minY']; i < grid['maxY']; i++) {
            outStr += i.toString() + "|";
            for (let j = grid['minX']; j < grid['maxX']; j++) {
                outStr += board[i][j];
            }
            outStr += "\n";
        }
        console.log(outStr);
        return
    }
    
    function checkCell(cell) {
        return cell == "*" ? 1 : 0;
    }

    function countLiveNeighbors(board, x, y) {
        let count = 0;
        // Edges
        let topEnd = y == 0;
        let bottomEnd = y == board.length - 1;
        let leftEnd = x == 0;
        let rightEnd = x == board[0].length - 1;

        // Above
        if (!topEnd) {
            if (!leftEnd) {
                count += checkCell(board[y-1][x-1]);
            }
            count += checkCell(board[y-1][x]);
            if (!rightEnd) {
                count += checkCell(board[y-1][x+1]);
            }
        }
        // Same Row
        if (!leftEnd) {
            count += checkCell(board[y][x-1]);
        }
        if (!rightEnd) {
            count += checkCell(board[y][x+1]);
        }
        // Below
        if (!bottomEnd) {
            if (!leftEnd) {
                count += checkCell(board[y+1][x-1]);
            }
            count += checkCell(board[y+1][x]);
            if (!rightEnd) {
                count += checkCell(board[y+1][x+1]);
            }
        }

        return count;
    }

    function calculateGrid(board) {
        let minX = board[0].length, maxX = 0, minY = board.length, maxY = 0;

        for (let y = 0; y < board.length; y++) {
            for (let x = 0; x < board[0].length; x++) {
                if (board[y][x] == "*") {
                    minX = x < minX ? x : minX;
                    maxX = x+1 > maxX ? x+1 : maxX;
                    minY = y < minY ? y : minY;
                    maxY = y+1 > maxY ? y+1 : maxY;
                }
            }
        }

        return {
            'minX' : minX,
            'maxX' : maxX,
            'minY' : minY,
            'maxY' : maxY
        };
    }

    // Build Initial 2D array.
    let minX = Number.POSITIVE_INFINITY, minY = Number.POSITIVE_INFINITY;
    let maxX = 0, maxY = 0;

    coords.forEach((liveCell) => {
        minX = Math.min(liveCell[0], minX);
        maxX = Math.max(liveCell[0], maxX);
        minY = Math.min(liveCell[1], minY);
        maxY = Math.max(liveCell[1], maxY);
    });

    let board = Array(maxY+1).fill(Array(maxX+1).fill("."));
    coords.forEach((liveCell) => {
        board[liveCell[1]][liveCell[0]] = "*";
    });

    console.log("Step 0");
    printBoard(board, {'minX' : minX, 'maxX' : maxX+1, 'minY' : minY-1, 'maxY' : maxY+1});

    for (let step = 0; step < steps; step++) {
        let newBoard = board.map((row) => {return row.map((val) => {return val})});

        // Check live/dead flips on current board.
        for (let y = 0; y < board.length; y++) {
            for (let x = 0; x < board[0].length; x++) {
                // Any dead cell with exactly three live neighbors becomes a live cell.
                if (board[y][x] == '.' && countLiveNeighbors(board, x, y) == 3) {
                    newBoard[y][x] = '*'
                    minX = Math.min(x, minX);
                    minY = Math.min(y, minY);
                }
                // Any live cell with less than two or more than three live neighbors dies.
                else if (board[y][x] == "*") {
                    let liveNeighbors = countLiveNeighbors(board, x, y);
                    newBoard[y][x] = (liveNeighbors == 2 || liveNeighbors == 3) ? "*" : ".";
                }
            }
        }

        // Edge Checks
        // Do right, then left and add columns as needed, then do right then left and add rows as needed.
        // Right Check
        let rightEdge = board[0].length - 1;
        for (let y = 1; y < board.length-1; y++) {
            if (checkCell(board[y-1][rightEdge]) && checkCell(board[y][rightEdge]) && checkCell(board[y+1][rightEdge])) {
                if (board[0].length == newBoard[0].length){
                    newBoard.forEach((row) => {
                        row.push(".");
                    });
                }
                newBoard[y][board[0].length] = "*";
            }
        }

        // Left Check
        let leftEdgeShifted = false;
        for (let y = 1; y < board.length-1; y++) {
            if (checkCell(board[y-1][0]) && checkCell(board[y][0]) && checkCell(board[y+1][0])) {
                if (!leftEdgeShifted) {
                    newBoard.forEach((row) => {
                        row.splice(0, 0, ".");
                    });
                    leftEdgeShifted = true;
                }
                newBoard[y][0] = "*";
            }
        }

        // Bottom Check
        let bottomEdge = board.length - 1;
        for (let x = 1; x < board[0].length-1; x++) {
            if (checkCell(board[bottomEdge][x-1]) && checkCell(board[bottomEdge][x]) && checkCell(board[bottomEdge][x+1])) {
                if (board.length == newBoard.length){
                    newBoard.push(Array(board[0].length).fill("."));
                }
                newBoard[bottomEdge][x] = "*";
            }
        }

        // Top Check
        let topEdgeShifted = false;
        for (let x = 1; x < board[0].length-1; x++) {
            if (checkCell(board[0][x-1]) && checkCell(board[0][x]) && checkCell(board[0][x+1])) {
                if (!topEdgeShifted) {
                    newBoard.splice(Array(board[0].length).fill("."));
                    topEdgeShifted = true;
                }
                newBoard[0][x] = "*";
            }
        }

        board = newBoard.map((row) => {return row.map((val) => {return val})});
        let grid = calculateGrid(board);
        
        console.log("Step", step+1);
        printBoard(board, grid);
    }

    return;
}

gameOfLife([[3, 3], [3, 4], [4, 3], [4, 5], [4, 4]], 5);