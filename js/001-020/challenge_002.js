/*
Given an array of integers, return a new array such that each element at index i of the new array is
the product of all the numbers in the original array except the one at i

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6]
*/

// Naive solution involves nested loops, resulting in O(n^2) time complexity.
// The below solution involves getting a total product, then dividing to get the product at each index. This completes in O(n) time complexity.
function productWithoutElement(numArray) {
    // Need to know where any zeros are to determine all products.
    const zeroLocations = [];

    // Multiply all non-zero numbers into a single product. Get indices of any zeros.
    let totalProduct = 1;
    numArray.forEach((num, index) => {
        if (num == 0) {
            zeroLocations.push(index);
        }
        else {
            totalProduct *= num;
        }
    });

    // Now fill an array based on how many zeros there are, then return it.
    const products = [];
    switch (zeroLocations.length) {
        case 0: // No zeros: Each product is the totalProduct divided by the number in the input array at the same index.
            numArray.forEach((num) => {
                products.push(totalProduct / num);
            });
            break;
        case 1: // One zero: Each product is 0 except for the index where the 0 is at, which is totalProduct.
            for (let i = 0; i < numArray.length; i++) {
                i == zeroLocations[0] ? products.push(totalProduct) : products.push(0);
            }
            break;
        default: // More than one zero: Each product is 0.
            for (let i = 0; i < numArray.length; i++) {
                products.push(0);
            }
    }
    return products;
}

console.log(productWithoutElement([1, 2, 3, 4, 5]));
console.log(productWithoutElement([1, 2, 3, 4, 5, 0]));
console.log(productWithoutElement([1, 2, 0, 3, 4, 5, 0]));