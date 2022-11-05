/*
You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board
where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.
*/

function arrangeQueens(N, board=[]) {
    // Subroutine to determine if a board is valid.
    function isValid(board) {
        let newQueenRow = board.length - 1;
        let newQueenCol = board[newQueenRow];

        // Compare the column value in the new row to previous rows' column values.
        // If the difference is 0 or equal to the row difference in any case, the board is not valid.
        for (let row = 0; row < newQueenRow; row++) {
            let colDiff = Math.abs(newQueenCol - board[row]);
            if (colDiff == 0 || colDiff == newQueenRow - row) {
                return false;
            }
        }

        return true;
    }

    // Sanity Checks
    if (!N instanceof Number) {
        throw "N must be a number.";
    }
    if (N < 0) {
        return 0;
    }

    // Complete Board.
    if (N == board.length) {
        return 1;
    }

    let count = 0;
    for (let column = 0; column < N; column++) {
        board.push(column);
        if (isValid(board)) {
            count += arrangeQueens(N, board);
        }
        board.pop();
    }

    return count;
}

console.log(arrangeQueens(8));