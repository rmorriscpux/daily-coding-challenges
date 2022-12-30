/*
Suppose you have a multiplication table that is N by N.
That is, a 2D array where the value at the i-th row and j-th column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).

Given integers N and X, write a function that returns the number of times X appears as a value in an N by N multiplication table.

For example, given N = 6 and X = 12, you should return 4, since the multiplication table looks like this:

| 1 | 2 | 3 | 4 | 5 | 6 |

| 2 | 4 | 6 | 8 | 10 | 12 |

| 3 | 6 | 9 | 12 | 15 | 18 |

| 4 | 8 | 12 | 16 | 20 | 24 |

| 5 | 10 | 15 | 20 | 25 | 30 |

| 6 | 12 | 18 | 24 | 30 | 36 |

And there are 4 12's in the table.
*/

function multCount(N, X) {
    if (!typeof(N) == 'number' || !typeof(X) == 'number') throw TypeError("N and X must be numbers.");
    if (N <= 0 || X <= 0) throw RangeError("N and X must be positive.");

    let count = 0;
    const sqrtX = Math.sqrt(X);

    if (sqrtX > N) {
        return count;
    }

    for (let multiple = 1; multiple < sqrtX; multiple++) {
        if (X % multiple == 0 && X / multiple <= N) {
            count += 2;
        }
    }

    if (sqrtX == Math.floor(sqrtX)) {
        count++;
    }

    return count;
}

console.log(multCount(6, 12));
console.log(multCount(5, 12));
console.log(multCount(2, 8));
console.log(multCount(1, 1));
console.log(multCount(6, 4));
console.log(multCount(3, 6));