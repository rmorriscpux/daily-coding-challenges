/*
You are given an array of non-negative integers that represents a two-dimensional elevation map
where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index
(we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
*/

function waterFilled(heightArray) {
    // The trick is to alternate approaches from the beginning and the end, going from low to high.
    // Start from the lowest height, switch when a wall higher than the other side is reached.
    let leftPtr = 0, rightPtr = heightArray.length - 1;

    let fillAmount = 0;

    let maxLeft = 0, maxRight = 0;

    while (leftPtr <= rightPtr) {
        if (heightArray[leftPtr] <= heightArray[rightPtr]) {
            // The left wall side is lower or the same height. Approach from the left.
            if (heightArray[leftPtr] >= maxLeft) {
                // Shift the maximum height on the left side to where left_ptr is now.
                maxLeft = heightArray[leftPtr];
            } else {
                // height at leftPtr is lower than the current max height. Add to the fill.
                fillAmount += maxLeft - heightArray[leftPtr];
            }
            leftPtr++;
        } else {
            // The right wall side is lower. Approach from the right.
            if (heightArray[rightPtr] >= maxRight) {
                // Shift the maximum height on the right side to where right_ptr is now.
                maxRight = heightArray[rightPtr];
            } else {
                // Height at rightPtr is lower than the current max height. Add to the fill.
                fillAmount += maxRight - heightArray[rightPtr];
            }
            rightPtr--;
        }
    }

    return fillAmount;
}

console.log(waterFilled([3, 0, 1, 4, 0, 5, 0, 2]));