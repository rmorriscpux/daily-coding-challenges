/*
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
*/

function delay(n, f){
    // Delay portion.
    const start = Date.now();
    let end = Date.now();
    do {
        end = Date.now();
    } while (end - start < n);
    // Function portion.
    const argArray = Array.prototype.slice.call(arguments);
    return f(...argArray.slice(2));
}

function printAndReturnSquare(x) {
    console.log(x * x);
    return x * x;
}

console.log("Start Anon");
delay(5000, () => {console.log("Hello World");});
console.log("Start Square");
delay(3000, printAndReturnSquare, 3);