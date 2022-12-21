/*
A sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.
*/

function findIndex(numArr, element) {
    if (element >= numArr[0]) {
        for (let i = 0; i < numArr.length; i++) {
            if (numArr[i] == element) {
                return i;
            }
            if (numArr[i] > element || i+1 == numArr.length || numArr[i] > numArr[i+1]) {
                return null;
            }
        }
    }
    else {
        for (let i = numArr.length-1; i >= 0; i--) {
            if (numArr[i] == element) {
                return i;
            }
            if (numArr[i] < element || i-1 == -1 || numArr[i] < numArr[i-1]) {
                return null;
            }
        }
    }
}