/*
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
*/

function minRooms(timeIntervals) {
    timeIntervals.forEach((lectureTime) => {
        if (lectureTime.length != 2) throw RangeError("Incorrect Lecture Time Length");
        if ((isNaN(lectureTime[0]) || isNaN(lectureTime[1]))) throw TypeError("All lecture times must be numbers.");
        if (lectureTime[0] >= lectureTime[1]) throw EvalError("Lecture start time cannot be before end time.");
    });

    timeIntervals.sort((a, b) => a[0] - b[0]);

    let maxRooms = 0;
    const endQueue = [];

    timeIntervals.forEach((lectureTime) => {
        while (endQueue.length > 0) {
            if (endQueue[0] <= lectureTime[0]) {
                endQueue.shift();
            } else {
                break;
            }
        }
        endQueue.push(lectureTime[1]);
        maxRooms = Math.max(maxRooms, endQueue.length);
    });

    return maxRooms;
}

console.log(minRooms([[30, 75], [0, 50], [60, 150]]));