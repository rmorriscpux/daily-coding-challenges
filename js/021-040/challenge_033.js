/*
Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

    2
    1.5
    2
    3.5
    2
    2
    2
*/

function runningMedian(numSequence) {
    if (numSequence.length == 0) {
        return;
    }
    
    const sortedSequence = [];
    numSequence.forEach((num) => {
        // Go backward until we find a valid position to splice so that the array remains sorted.
        // A slightly quicker, though more complicated sort involves starting in the middle, then going forward or backward.
        let insertIndex = sortedSequence.length;
        while (insertIndex > 0 && sortedSequence[insertIndex-1] > num) {
            insertIndex--;
        }
        sortedSequence.splice(insertIndex, 0, num);
        // Now get the median.
        let pivotIndex = Math.floor(sortedSequence.length / 2);
        if (sortedSequence.length % 2) { // Odd - Middle number.
            console.log(sortedSequence[pivotIndex]);
        }
        else { // Even - Average of two middle numbers.
            console.log((sortedSequence[pivotIndex] + sortedSequence[pivotIndex-1]) / 2);
        }
    });

    return;
}

runningMedian([2, 1, 5, 7, 2, 0, 5]);