/*
Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true,
since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum.
*/

function splitSum(intList) {
    function sum(intList) {
        let total = 0;
        for (int of intList) {
            total += int;
        }
        return total;
    }

    function rSplitSum(sumList, remainingList, targetSum) {
        if(sum(sumList) == targetSum) {
            return true;
        }

        if (remainingList.length == 0 || sum(sumList) > targetSum) {
            return false;
        }

        for (let i = 0; i < remainingList.length; i++) {
            sumList.push(remainingList[i]);
            if (rSplitSum(sumList, remainingList.slice(0, i).concat(remainingList.slice(i+1)), targetSum)) {
                return true;
            }
            sumList.pop();
        }

        return false;
    }

    let total = sum(intList);

    if (total % 2 == 1) {
        return false;
    }

    return rSplitSum([], intList, Math.floor(total / 2));
}

console.log(splitSum([15, 5, 20, 10, 35, 15, 10]));
console.log(splitSum([15, 5, 20, 10, 35]));