/*
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2
*/

function calcSteps(n) {
    function fibonnaci(k, fib_list) {
        if (k <= 1) {
            fib_list[k] = 1;
        }

        if (fib_list[k] != -1) {
            return fib_list[k];
        }

        fib_list[k] = fibonnaci(k-1, fib_list) + fibonnaci(k-2, fib_list);
        return fib_list[k];
    }

    if (isNaN(n) || n < 0){
        return 0;
    }

    n = Math.floor(n);

    const fib_list = []
    for (let i = 0; i < n+1; i++){
        fib_list.push(-1);
    }

    return fibonnaci(n, fib_list);
}

console.log(calcSteps(0))
console.log(calcSteps(1))
console.log(calcSteps(2))
console.log(calcSteps(3))
console.log(calcSteps(4))
console.log(calcSteps(5))
console.log(calcSteps(6))
console.log(calcSteps(7))

/*
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X?
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
*/

function calcMultSteps(n, options) {
    function polyFib(k, waysList, numOptions) {
        if (waysList[k] != -1) {
            return waysList[k];
        }

        waysList[k] = polyFib(k-1, waysList, numOptions);
        for (let i = 1; i < numOptions; i++){
            waysList[k] += polyFib(k-(i+2), waysList, numOptions);
        }
        
        return waysList[k];
    }

    if (isNaN(n) || n < 0) {
        return 0;
    }

    n = Math.floor(n);

    options.forEach((o) => {
        if (isNaN(o) || o < 1) {
            return 0;
        }
        o = Math.floor(o);
    });
    options.sort((a, b) => {return a-b});

    const waysList = [];
    for (let i = 0; i < n+1; i++){
        if (i <= options[0]) {
            waysList.push(1);
        }
        else {
            waysList.push(-1);
        }
    }

    for (let i = 1; i < options.length; i++) {
        for (let j = options[i-1]; j < options[i]-1; j++){
            polyFib(j+1, waysList, i);
        }
        waysList[options[i]] = waysList[options[i-1]] + 1;
    }

    polyFib(n, waysList, options.length);
    return waysList[n];
}

console.log("==========");
console.log(calcMultSteps(7, [1,2,3]));
console.log(calcMultSteps(10, [1,3,5]));