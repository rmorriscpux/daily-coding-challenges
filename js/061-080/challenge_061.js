/*
Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
*/

function pow(x, y) {
    // Universal Cases: 0^y = 0 where y > 0, 1 where y == 0, error where y < 0. 
    //                  x^0 = 1 where x >=0, -1 where x < 0.
    if (x == 0) {
        if (y == 0) {
            return 1;
        }
        else if (y < 0) {
            throw "0.0 cannot be raised to a negative power."
        }
        return 0;
    }
    if (y == 0) {
        return x > 0 ? 1 : -1;
    }

    let power = 1;
    let result = x;

    // Exponentially increase the result until we reach a point where doubling the exponent exceeds y.
    while (power * 2 <= Math.abs(y)) {
        result *= result;
        power *= 2;
    }

    // Multiply in the remaining exponent via recursive call.
    result *= pow(x, Math.abs(y) - power);

    //  Negative power means inverse result.
    return y < 0 ? 1 / result : result;
}

console.log(pow(2, 10)) // 1024
console.log(pow(10, 3)) // 1000
console.log(pow(3, 5))  // 243
console.log(pow(-3, 5)) // -243
console.log(pow(2, -3)) // 0.125