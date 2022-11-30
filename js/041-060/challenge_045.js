/*
Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability,
implement a function rand7() that returns an integer from 1 to 7 (inclusive).
*/

// Base rand5() function that returns a random integer between 1 and 5 inclusive.
// Note that Math.ceil(Math.random() * 5) is not feasible because of the slight probability that Math.random() returns 0.
const rand5 = () => Math.floor(Math.random() * 5 + 1);

function rand7() {
    // Obtain a uniformly random draw between 1 and 25 by using rand5(). Sums one of {0, 5, 10, 15, 20} with one of {1, 2, 3, 4, 5}
    // To scale, redraw if we get a draw above 21.
    // Average number of loop iterations = Σ(4/25)^k for integers k from 1 to ∞, which is approximately 0.1905.
    // This means the average number of calls to rand5(), including the initial setup, is 2.3810.
    let draw = (rand5() - 1) * 5 + rand5();
    while (draw > 21) {
        draw = (rand5() - 1) * 5 + rand5();
    }

    // draw is between 0 and 20. Use modulo 7 to return a number between 1 and 7.
    return (draw % 7) + 1;
}