/*
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
*/

function largestNonAdjacentSum(numArray) {
    let prevSum = 0, sum = 0;

    // Compare in a cascading fashion so that in the end adjacent numbers are not added together.
    numArray.forEach((num) => {
        let tempSum = sum;
        sum = Math.max(sum, prevSum + num);
        prevSum = tempSum;
    });

    return sum;
}

console.log(largestNonAdjacentSum([2, 4, 6, 2, 5]));
console.log(largestNonAdjacentSum([5, 1, 1, 5]));