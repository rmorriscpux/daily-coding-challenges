/*
Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
*/

function getSingleInteger(intArray) {
    const uniqueIntegers = new Set();
    let tripleSum = 0;
    let total = 0;

    intArray.forEach((i) => {
        let startSize = uniqueIntegers.size;
        total += i;
        uniqueIntegers.add(i);
        if (startSize < uniqueIntegers.size) {
            tripleSum += i * 3;
        }
    });

    return (tripleSum - total) / 2;
}

console.log(getSingleInteger([6, 1, 3, 3, 3, 6, 6]));
console.log(getSingleInteger([13, 19, 13, 13]));