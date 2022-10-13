/*
Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
*/

function firstMissingPositive(numArray) {
    // Empty Array
    if (numArray.length == 0) {
        return 1;
    }

    let start = 0, end = numArray.length - 1;
    while (start < end) {
        if (numArray[start] > 0 && numArray[end] <= 0) {
            let temp = numArray[start];
            numArray[start] = numArray[end];
            numArray[end] = temp;
        }
        
        if (numArray[start] <= 0) {
            start++;
        }
        if (numArray[end] > 0) {
            end--;
        }
    }

    // Case where the entire array is non-positive.
    if (numArray[start] <= 0){
        return 1;
    }

    // Case where the array contains consecutive (not necessarily ordered) integers starting with 1.
    if (Math.max(numArray) == numArray.length){
        return numArray.length + 1;
    }

    numArray = numArray.slice(start);

    numArray.forEach((num) => {
        let absNum = Math.abs(num);
        if (absNum-1 < numArray.length){
            numArray[absNum-1] *= -1;
        }
    });

    for (let i = 0; i < numArray.length; i++){
        if (numArray[i] > 0){
            return i + 1;
        }
    }
}

console.log(firstMissingPositive([3, 4, -1, 1]));
console.log(firstMissingPositive([1, 2, 0]));