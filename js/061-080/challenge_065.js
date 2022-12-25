/*
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]

You should print out the following:

1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12
*/

function spiral(matrix) {
    const N = matrix.length, M = matrix[0].length;

    const visited = matrix.map((row) => row.map((i) => false));

    function goRight(matrix, visited, x, y, M, N, outList) {
        while (true) {
            visited[y][x] = true;
            outList.push(matrix[y][x]);
            if (x >= M-1 || visited[y][x+1]) {
                break;
            }
            x++;
        }

        if (y < N-1 && !visited[y+1][x]) {
            goDown(matrix, visited, x, y+1, M, N, outList);
        }
        return;
    }

    function goDown(matrix, visited, x, y, M, N, outList) {
        while (true) {
            visited[y][x] = true;
            outList.push(matrix[y][x]);
            if (y >= N-1 || visited[y+1][x]) {
                break;
            }
            y++;
        }

        if (x > 0 && !visited[y][x-1]) {
            goLeft(matrix, visited, x-1, y, M, N, outList);
        }
        return;
    }

    function goLeft(matrix, visited, x, y, M, N, outList) {
        while (true) {
            visited[y][x] = true;
            outList.push(matrix[y][x]);
            if (x <= 0 || visited[y][x-1]) {
                break;
            }
            x--;
        }

        if (y > 0 && !visited[y-1][x]) {
            goUp(matrix, visited, x, y-1, M, N, outList);
        }
        return;
    }

    function goUp(matrix, visited, x, y, M, N, outList) {
        while (true) {
            visited[y][x] = true;
            outList.push(matrix[y][x]);
            if (y <= 0 || visited[y-1][x]) {
                break;
            }
            y--;
        }

        if (x < M-1 && !visited[y][x+1]) {
            goRight(matrix, visited, x+1, y, M, N, outList);
        }
        return;
    }

    const outList = [];

    goRight(matrix, visited, 0, 0, M, N, outList);

    console.log(...outList);
}

const matrix = [
    [1,  2,  3,  4,  5],
    [6,  7,  8,  9,  10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
];

spiral(matrix);