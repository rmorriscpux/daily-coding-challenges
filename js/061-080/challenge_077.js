/*
Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
*/

function mergeIntervals(intervalList) {
    const intervalStarts = {}, intervalEnds = {};

    for (interval of intervalList) {
        if (!Object.keys(intervalStarts).includes(interval[0].toString())) {
            intervalStarts[interval[0]] = 0;
        }
        intervalStarts[interval[0]]++;
        if (!Object.keys(intervalEnds).includes(interval[1].toString())) {
            intervalEnds[interval[1]] = 0;
        }
        intervalEnds[interval[1]]++;
    }

    let minStart = Math.min(...Object.keys(intervalStarts).map((n) => +n));
    let maxEnd = Math.max(...Object.keys(intervalEnds).map((n) => +n));
    const intervalStatusList = [];
    let intervalStatus = 0;
    for (let i = minStart; i < maxEnd+1; i++) {
        if (Object.keys(intervalStarts).includes(i.toString())) {
            intervalStatus += intervalStarts[i.toString()];
        }
        if (Object.keys(intervalEnds).includes(i.toString())) {
            intervalStatus -= intervalEnds[i.toString()];
        }
        intervalStatusList.push(intervalStatus);
    }

    let start = minStart;
    let end = null;

    const mergedList = [];
    for (let i = 1; i < intervalStatusList.length; i++) {
        if (intervalStatusList[i] > 0 && intervalStatusList[i-1] == 0) {
            start = minStart + i;
        }
        if (intervalStatusList[i] == 0 && intervalStatusList[i-1] > 0) {
            end = minStart + i;
            mergedList.push([start, end]);
        }
    }

    return mergedList;
}

console.log(mergeIntervals([[1, 3], [5, 8], [4, 10], [20, 25]]));
console.log(mergeIntervals([[1, 3], [5, 8], [20, 27], [4, 10], [20, 25]]));