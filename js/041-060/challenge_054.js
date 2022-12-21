/*
Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits.
The objective is to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

Implement an efficient sudoku solver.
*/

// Unfilled locations represented by '0'. No checks done here to validate the board.

function sudokuSolver(board) {
    // Shorthand function to get box coordinates for use in the boxFills dictionary.
    const boxCoords = (y, x) => `${y-y%3}-${x-x%3}`;

    //Backtracking recursive subroutine. As we go through, we want to keep track of which numbers are in each row, column, and box.
    function rSudokuSolver(board, rowFills, colFills, boxFills) {
        for (let i = 0; i < 9; i++) {
            for (let j = 0; j < 9; j++) {
                if (board[i][j] == 0) {
                    let boxKey = boxCoords(i, j);
                    for (let val = 1; val <= 9; val++) {
                        // Check if val (1 through 9) is not in the same row, column, or box.
                        if (!rowFills[i].has(val) &&
                            !colFills[j].has(val) &&
                            !boxFills[boxKey].has(val)) {
                                board[i][j] = val;
                                rowFills[i].add(val);
                                colFills[j].add(val);
                                boxFills[boxKey].add(val);
                                // Now check the recursive, and backtrack if we can't make a valid solution.
                                if (rSudokuSolver(board, rowFills, colFills, boxFills)) {
                                    return true;
                                }
                                else {
                                    board[i][j] = 0;
                                    rowFills[i].delete(val);
                                    colFills[j].delete(val);
                                    boxFills[boxKey].delete(val);
                                }
                            }
                    }
                    // At this point, no valid solutions can be made from the board given.
                    return false;
                }
            }
        }
        // At this point, the board is complete.
        return true;
    }

    // Set up objects of sets for row, col, and box fills.
    const rowFills = {}, colFills = {}, boxFills = {};

    for (let i = 0; i < 9; i++) {
        rowFills[i.toString()] = new Set();
        colFills[i.toString()] = new Set();
        boxFills[boxCoords(i, (i%3)*3)] = new Set();
    }

    // Fill in the sets with already filled values.
    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            if (board[i][j] != 0) {
                rowFills[i].add(board[i][j]);
                colFills[j].add(board[i][j]);
                boxFills[boxCoords(i, j)].add(board[i][j]);
            }
        }
    }

    // Now that we're set up, go through the recursive function.
    rSudokuSolver(board, rowFills, colFills, boxFills);

    return;
}

// Print function
function printSudoku(board) {
    console.log("|-----+-----+-----|");
    for (let i = 0; i < 9; i++) {
        let outLine = "|";
        for (let j = 0; j < 9; j++) {
            outLine = outLine.concat(board[i][j].toString());
            outLine = j % 3 == 2 ? outLine.concat("|") : outLine.concat(" ");
        }
        console.log(outLine);
        if (i % 3 == 2) {
            console.log("|-----+-----+-----|");
        }
    }
    return;
}

let board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
];

printSudoku(board);

sudokuSolver(board);

console.log("============================");
printSudoku(board)