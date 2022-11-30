/*
We can determine how "out of order" an array A is by counting the number of inversions it has.
Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions.
The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3).
The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.
*/

function countInversions(numArr) {
    // Internal merge sort function that counts inversions in addition to sorting.
    function mergeArrays(arr1Info, arr2Info) {
        const arr1 = arr1Info[0], arr2 = arr2Info[0];
        let inversions = arr1Info[1] + arr2Info[1];

        const mergedArray = [];
        let i1 = 0, i2 = 0;

        while (i1 < arr1.length && i2 < arr2.length) {
            if (arr1[i1] < arr2[i2]) {
                mergedArray.push(arr1[i1]);
                i1++;
            }
            else {
                mergedArray.push(arr2[i2]);
                i2++;
                inversions += arr1.length - i1;
            }
        }

        while (i1 < arr1.length) {
            mergedArray.push(arr1[i1]);
            i1++;
        }
        while (i2 < arr2.length) {
            mergedArray.push(arr2[i2]);
            i2++;
        }

        return [mergedArray, inversions];
    }

    function rCountInversions(numArr) {
        if (numArr.length <= 1) {
            return [numArr, 0];
        }

        // Split the array and count the inversions within each sub array.
        let middle = Math.floor(numArr.length / 2);
        const arr1Info = rCountInversions(numArr.slice(0, middle));
        const arr2Info = rCountInversions(numArr.slice(middle));
        // Finally, merge the results of the two split arrays.
        return mergeArrays(arr1Info, arr2Info);
    }

    // Only return the inversion count.
    return rCountInversions(numArr)[1];
}

console.log(countInversions([2, 4, 1, 3, 5]));
console.log(countInversions([5, 4, 3, 2, 1]));