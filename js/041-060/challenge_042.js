/*
Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
*/

function subSumSet(S, k) {
    // Recursive function to get sum.
    function rSubSumSet(curList, remainingList, curSum, targetSum) {
        // Good end condition.
        if (curSum == targetSum) {
            return curList;
        }
        // Bad end condition.
        else if (curSum > targetSum || remainingList.length == 0) {
            return null;
        }
        
        let result = null;
        for (let i = 0; i < remainingList.length; i++) {
            curList.push(remainingList[i]);
            result = rSubSumSet(curList, remainingList.slice(0, i).concat(remainingList.slice(i+1)), curSum + remainingList[i], targetSum);
            if (result != null) {
                return result;
            }
            curList.pop();
        }
        
        return result;
    }

    // Sort list descending.
    S.sort((a, b) => b - a);
    // Begin where all numbers are <= k.
    for (let i = 0; i < S.length; i++) {
        if (S[i] <= k) {
            return rSubSumSet([], S.slice(i), 0, k);
        }
    }
    // All integers in S are greater than k.
    return null;
}

console.log(subSumSet([12, 1, 61, 5, 9, 2], 24));
console.log(subSumSet([12, 1, 61, 5, 9, 2], 25));