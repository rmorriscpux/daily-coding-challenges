/*
Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability,
implement a function rand5() that returns an integer from 1 to 5 (inclusive).
*/

// Function that returns a random integer between 1 and 7 uniformly.
rand7 = () => Math.floor(Math.random() * 7) + 1;

// Version 1: Fewer average calls to rand7(), but with a higher volatility.
function rand5_1() {
    let randNum = rand7();

    // To scale, redraw if we get a draw above 5.
    // Average number of loop iterations = Σ(2/7)^k for integers k from 1 to ∞, which is approximately 0.6665.
    // This means the average number of calls to rand7(), including the initial setup, is 1.6665.
    while (randNum > 5) {
        randNum = rand7();
    }

    return randNum;
}

// Version 2: More average calls to rand7(), but with a lower volatility.
function rand5_2() {
    let randNum = (rand7() - 1) * 7 + rand7();

    // To scale, redraw if we get a draw above 45.
    // Average number of loop iterations = Σ(4/49)^k for integers k from 1 to ∞, which is approximately 0.0889.
    // This means the average number of calls to rand7(), including the initial setup, is 2.1778.
    while (randNum > 45) {
        randNum = (rand7() - 1) * 7 + rand7();
    }

    return (randNum % 5) + 1;
}

// Select function to use and number of trials to run in test here.
const rand5 = rand5_1;
const trials = 100000;

let results = {};
for (let i = 1; i < 6; i++){
    results[i] = 0;
}
for (let i = 1; i < trials; i++){
    r = rand5();
    results[r]++;
}
console.log(trials, "Trials:");
console.log(results)