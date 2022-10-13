/*
A builder is looking to build a row of N houses that can be of K different colors.
He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.
*/

function minCost(houseColorMatrix) {
    function rMinCost(houseColorMatrix, result, houseNum, prevColor=-1, cost=0, colorSequence=[]) {
        if (houseNum == houseColorMatrix.length) {
            result.push({'cost': cost, 'color sequence': colorSequence});
            return;
        }

        for (let i = 0; i < houseColorMatrix[houseNum].length; i++) {
            if (i != prevColor) {
                rMinCost(houseColorMatrix, result, houseNum+1, i, cost+houseColorMatrix[houseNum][i], colorSequence.concat([i]));
            }
        }
        return;
    }

    const houseColors = [];
    rMinCost(houseColorMatrix, houseColors, 0);
    let minIndex = 0;
    for (let i = 1; i < houseColors.length; i++) {
        if (houseColors[i]['cost'] < houseColors[minIndex]['cost']) {
            minIndex = i;
        }
    }
    return houseColors[minIndex];
}

const arr = [
    [1,2,3,4],
    [1,2,1,0],
    [6,1,1,5],
    [2,3,5,5]
];

console.log(minCost(arr));