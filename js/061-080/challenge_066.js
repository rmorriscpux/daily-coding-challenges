/*
Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0).
You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.
*/

function tossBiased(coinBias) {
    if (coinBias < 0 || coinBias >= 1 || !(typeof(coinBias) == 'number')) throw RangeError("coinBias must be a number between 0 inclusive and 1 exclusive.");

    return Math.random() >= coinBias ? 1 : 0;
}

const trials = 100000;
const count = [0, 0];
const bias = Math.random();
for (let i = 0; i < trials; i++) {
    count[tossBiased(bias)]++;
}

console.log("Coin Bias: %f\n   Trials: %d\n   Zeroes: %d\n     Ones: %d", bias, trials, count[0], count[1]);