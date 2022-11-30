/*
Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport,
compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries,
return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL',
you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A',
you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary.
However, the first one is lexicographically smaller.
*/

function buildItinerary(flightsList, startLocation) {
    // Recursive subroutine to build the itinerary.
    function rBuildItinerary(flights, itinerary) {
        // Terminator condition.
        if (flights.length == 0) {
            return itinerary;
        }

        for (let i = 0; i < flights.length; i++) {
            let flt = flights[i];
            // Add the current landing point to the itinerary
            itinerary.push(flt[1]);
            // Determine if the takeoff location is the same as the last point in the itinerary.
            if (flt[0] == itinerary[itinerary.length - 2]) {
                // Make new list excluding the flight used, and recur with that list.
                let flightsLeft = flights.slice(0, i).concat(flights.slice(i+1));
                return rBuildItinerary(flightsLeft, itinerary);
            }
            // Pop landing for next cycle.
            itinerary.pop();
        }
        // Loop complete. No valid itinerary exists.
        return null;
    }
    // Sort so flights are in order lexiconographically.
    flightsList.sort((a, b) => a[0] != b[0] ? a[0].localeCompare(b[0]) : a[1].localeCompare(b[1]));
    // Starting condition.
    let itinerary = null;
    for (let i = 0; i < flightsList.length; i++) {
        if (flightsList[i][0] == startLocation) {
            itinerary = rBuildItinerary(flightsList.slice(0, i).concat(flightsList.slice(i+1)), flightsList[i]);
        }
        if (itinerary != null) {
            break;
        }
    }

    return itinerary;
}

console.log(buildItinerary([['SFO', 'HKO'], ['YYZ', 'SFO'], ['YUL', 'YYZ'], ['HKO', 'ORD']], 'YUL'))
console.log(buildItinerary([['SFO', 'COM'], ['COM', 'YYZ']], 'COM'))
console.log(buildItinerary([['A', 'C'], ['A', 'B'], ['B', 'C'], ['C', 'A']], 'A'))