/*
Determine the value of pi using a Monte Carlo method. (i.e. taking a set of random values to get a deterministic result)
*/

// Area of a circle = pi * r^2. On a graph, the circumference can be represented as all points where r^2 = x^2 + y^2.
// Therefore, by taking a random x and y between 0 and 1 and determining if they're inside a unit circle (r=1),
// over enough trials the ratio of points inside the circle will be approximately pi / 4.

function monteCarloPi(trials) {
    let count = 0;
    for (let i = 0; i < trials; i++) {
        if (Math.random() ** 2 + Math.random() ** 2 <= 1) {
            count++;
        }
    }
    return count / trials * 4;
}

console.log(monteCarloPi(1000000));