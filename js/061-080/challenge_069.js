/*
Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
*/

function largestMultOfThree(intList) {
    if (intList.length < 3) throw RangeError("List too short.");

    // Sorting in place. If you want to retain the original order, copy the array first.
    intList.sort((a, b) => a - b);

    let l = intList.length; // For brevity. :-)

    // Case: All values are negative.
    if (intList[l-1] < 0) {
        return intList[l-1] * intList[l-2] * intList[l-3];
    }
    // Case: Highest value is 0.
    else if (intList[l-1] == 0) {
        return 0
    }
    // Case: Positive values exist.
    else {
        return Math.max(intList[l-1] * intList[l-2] * intList[l-3], intList[l-1] * intList[0] * intList[1]);
    }
}