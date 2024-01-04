'''
A group of houses is connected to the main water plant by means of a set of pipes.
A house can either be connected by a set of pipes extending directly to the plant, or indirectly by a pipe to a nearby house which is otherwise connected.

For example, here is a possible configuration, where A, B, and C are houses, and arrows represent pipes: A <--> B <--> C <--> plant

Each pipe has an associated cost, which the utility company would like to minimize.
Given an undirected graph of pipe connections, return the lowest cost configuration of pipes such that each house has access to water.

In the following setup, for example, we can remove all but the pipes from plant to A, plant to B, and B to C, for a total cost of 16.

pipes = {
    'plant': {'A': 1, 'B': 5, 'C': 20},
    'A': {'C': 15},
    'B': {'C': 10},
    'C': {}
}
'''

def lowestConnectionCost(pipes: dict[str, dict[str, int]]) -> int:
    def rLowestConnectionCost(pipes: dict[str, dict[str, int]], remaining_houses: set[str], total_cost: int=0) -> int:
        if not remaining_houses:
            # Return total_cost when no houses are left to connect.
            return total_cost
        
        costs = []
        for start in set(pipes.keys()).difference(remaining_houses):
            connectable_houses = pipes[start].keys() & remaining_houses
            for next in connectable_houses:
                costs.append(rLowestConnectionCost(pipes, remaining_houses.difference({next}), total_cost + pipes[start][next]))
        # Return the lowest cost from this iteration.
        return min(costs)
    
    return rLowestConnectionCost(pipes, set(pipes.keys()).difference({'plant'}))

if __name__ == "__main__":
    pipes = {
        'plant': {'A': 1, 'B': 5, 'C': 20},
        'A': {'C': 15},
        'B': {'C': 10},
        'C': {}
    }

    print(lowestConnectionCost(pipes))