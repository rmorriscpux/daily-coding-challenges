'''
Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport,
compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries,
return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL',
you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A',
you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary.
However, the first one is lexicographically smaller.
'''

from typing import List, Tuple
import copy # In this implementation, we're not going to modify the original 'flights' list.

def buildItinerary(flights : List[Tuple[str, str]], start : str):
    # Recursive subroutine to build the itinerary. Will call with an empty list.
    def rBuildItinerary(flights, itinerary):
        # Terminator: All flights have been used.
        if len(flights) == 0:
            return itinerary

        for i, (takeoff, landing) in enumerate(flights):
            # Add the current landing point to the itinerary.
            itinerary.append(landing)
            # Determine if the takeoff location is the same as the last point in the itinerary.
            if takeoff == itinerary[-2]:
                # Make new list excluding the flight used, and recur with that list.
                flights_left = flights[:i] + flights[i+1:]
                return rBuildItinerary(flights_left, itinerary)
            # Pop landing for next cycle.
            itinerary.pop()
        else: # Loop Completion
            return None

    # Sort the flights lexicongraphically.
    sorted_flights = copy.deepcopy(flights)
    sorted_flights.sort()
    # Initiate recursive subroutine. This looks for valid takeoff options and returns the first full itinerary found, if applicable.
    final_itinerary = None
    for i, (takeoff, landing) in enumerate(sorted_flights):
        if takeoff == start:
            final_itinerary = rBuildItinerary(sorted_flights[:i] + sorted_flights[i+1:], [takeoff, landing])
            break
    return final_itinerary

print(buildItinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL'))
print(buildItinerary([('SFO', 'COM'), ('COM', 'YYZ')], 'COM'))
print(buildItinerary([('A', 'C'), ('A', 'B'), ('B', 'C'), ('C', 'A')], 'A'))
