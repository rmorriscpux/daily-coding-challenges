/*
Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a possible arbitrage:
that is, whether there is some sequence of trades you can make, starting with some amount A of any currency,
so that you can end up with some amount greater than A of that currency.

There are no transaction costs and you can trade fractional quantities.
*/

function exchangeArbitrage(exchangeTable) {
    // Work with the negative natural log of each exchange rate for Bellman-Ford check.
    const logTable = exchangeTable.map((row) => row.map((x) => -Math.log(x)));
    // JS shortcut for making a new array filled with a specific value the same length as the input array.
    const minDistance = exchangeTable.map(() => Number.POSITIVE_INFINITY);

    minDistance[0] = 0;

    // Relax edges.
    for (let i = 0; i < minDistance.length-1; i++) {
        for (let v = 0; v < minDistance.length; v++) {
            for (let w = 0; w < minDistance.length; w++) {
                if (minDistance[w] > minDistance[v] + logTable[v][w]) {
                    minDistance[w] = minDistance[v] + logTable[v][w];
                }
            }
        }
    }

    // If we can still relax edges, then we have a negative cycle (i.e. arbitage)
    for (let v = 0; v < minDistance.length; v++) {
        for (let w = 0; w < minDistance.length; w++) {
            if (minDistance[w] > minDistance[v] + logTable[v][w]) {
                return true;
            }
        }
    }

    return false;
}

const table1 = [
    [1, 2, 5],
    [0.5, 1, 4],
    [0.2, 0.25, 1]
];

const table2 = [
    [1, 2, 4],
    [0.5, 1, 2],
    [0.25, 0.5, 1]
];

console.log(exchangeArbitrage(table1));
console.log(exchangeArbitrage(table2));