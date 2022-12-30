/*
Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
*/

function longestIncreasingSubseq(numArr) {
    function rLongestIncreasingSubseq(numArr, startIndex, countPerIndex) {
        if (startIndex == numArr.length) {
            return 0;
        }

        let maxCount = 1;
        let count = 0;

        for (let i = startIndex+1; i < numArr.length; i++) {
            if (numArr[i] > numArr[startIndex]) {
                if (countPerIndex[i] > 0) {
                    count = countPerIndex[i];
                }
                else {
                    count = rLongestIncreasingSubseq(numArr, i, countPerIndex) + 1;
                    countPerIndex[i] = count;
                }

                maxCount = count > maxCount ? count : maxCount;
            } 
        }

        return maxCount;
    }

    const countPerIndex = numArr.map((n) => 0);
    return rLongestIncreasingSubseq(numArr, 0, countPerIndex);
}

console.log(longestIncreasingSubseq([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]));