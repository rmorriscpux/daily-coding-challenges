/*
Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.
*/

function canMakeNonDecreasing(intArr) {
    if (intArr.length <= 2) {
        return true;
    }

    let hasDecreasingPair = false;

    for (let i = 1; i < intArr.length; i++) {
        if (intArr[i] < intArr[i-1]) {
            if (hasDecreasingPair) {
                return false;
            }
            hasDecreasingPair = true;
        }
    }

    return true;
}

console.log(canMakeNonDecreasing([10, 5, 7]));
console.log(canMakeNonDecreasing([10, 5, 1]));