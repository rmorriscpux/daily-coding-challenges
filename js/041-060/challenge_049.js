/*
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
*/

function getMaxSum(numArray) {
    // For when list is all negative or 0, or array is empty.
    if (numArray.length == 0 || Math.max(...numArray) <= 0) {
        return 0;
    }

    let maxSum = Math.max(0, numArray[0]);
    let tempMaxSum = maxSum;
    // Traverses the list and maintains a max sum, discarding it if a larger contiguous sum comes along.
    for (let i = 1; i < numArray.length; i++) {
        tempMaxSum = Math.max(numArray[i], tempMaxSum + numArray[i]);
        maxSum = Math.max(maxSum, tempMaxSum);
    }

    return maxSum;
}

console.log(getMaxSum([34, -50, 42, 14, -5, 86]));
console.log(getMaxSum([-5, -1, -8, -9]));