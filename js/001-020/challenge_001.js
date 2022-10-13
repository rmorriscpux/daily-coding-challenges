/*
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
*/

function sumTwoToK(numList, k){
    for (let i = 0; i < numList.length-1; i++) {
        for (let j = i+1; j < numList.length; j++) {
            if (numList[i] + numList[j] == k) {
                return true
            }
        }
    }
    return false;
}

console.log(sumTwoToK([10, 15, 3, 7], 17));
console.log(sumTwoToK([10, 15, 3, 7], 18));
console.log(sumTwoToK([10, 15, 3, 7], 19));