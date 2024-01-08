'''
An imminent hurricane threatens the coastal town of Codeville. If at most two people can fit in a rescue boat,
and the maximum weight limit for a given boat is k, determine how many boats will be needed to save everyone.

For example, given a population with weights [100, 200, 150, 80] and a boat limit of 200, the smallest number of boats required will be three.
'''

from typing import List

def minBoats(population: List[int], k: int) -> int:
    def rMinBoats(remaining: List[int], k: int, boats: int=0) -> int:
        # Completion state. No remaining passengers left.
        if not remaining:
            return boats
        
        boat_weight = 0
        while remaining:
            # Add passengers until no more can be added.
            if boat_weight + remaining[0] > k:
                break
            boat_weight += remaining[0]
            remaining.pop(0)
        # Recur with one boat added and the passengers on it removed from the list.
        return rMinBoats(remaining, k, boats+1)
    
    sorted_population = sorted(population)
    if sorted_population:
        assert sorted_population[-1] <= k
    return rMinBoats(sorted_population, k)

if __name__ == "__main__":
    print(minBoats([100, 200, 150, 80], 200)) # 3