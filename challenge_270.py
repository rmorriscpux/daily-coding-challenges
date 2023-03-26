'''
A network consists of nodes labeled 0 to N. You are given a list of edges (a, b, t),
describing the time t it takes for a message to be sent from node a to node b.
Whenever a node receives a message, it immediately passes the message on to a neighboring node, if possible.

Assuming all nodes are connected, determine how long it will take for every node to receive a message that begins at node 0.

For example, given N = 5, and the following edges:

edges = [
    (0, 1, 5),
    (0, 2, 3),
    (0, 5, 4),
    (1, 3, 8),
    (2, 3, 1),
    (3, 5, 10),
    (3, 4, 5)
]
You should return 9, because propagating the message from 0 -> 2 -> 3 -> 4 will take that much time.
'''

from collections import namedtuple
from typing import List

Edge = namedtuple('Edge', ['a', 'b', 't'])

def reachAllNodes(edges: List[Edge[int, int, int]]) -> int:
    def reachNode(edges: List[Edge], cur_node: int, cur_time: int, node_times: list):
        for e in edges:
            # Check path time for every b where the current node equals a on the edge.
            if e.a == cur_node:
                time_to_b = cur_time + e.t
                if time_to_b < node_times[e.b]:
                    # Quicker path has been found. Set the new time to the node index and recur from there.
                    node_times[e.b] = time_to_b
                    reachNode(edges, e.b, time_to_b, node_times)
        return
    
    all_nodes = set(map(lambda e: e.a, edges)).union(set(map(lambda e: e.b, edges)))
    # Optional assertions.
    if not all(map(lambda n: 0 <= n < len(all_nodes), all_nodes)):
        raise ValueError("Incomplete Network.")
    if not all(map(lambda e: e.t >= 0, edges)):
        raise ValueError("Node message time cannot be less than zero.")
    # Setup - All node times set to infinity except node 0 which equals 0.
    node_times = [0] + [float('inf')] * (len(all_nodes) - 1)
    # Recursion to get minimum node times starting from node 0.
    reachNode(edges, 0, 0, node_times)

    max_time = max(node_times)
    # Node has not been reached if its index in the list is still infinity.
    if max_time == float('inf'):
        raise ValueError("Unreachable Nodes.")
    return max_time

edges = [
    Edge(0, 1, 5),
    Edge(0, 2, 3),
    Edge(0, 5, 4),
    Edge(1, 3, 8),
    Edge(2, 3, 1),
    Edge(3, 5, 10),
    Edge(3, 4, 5)
]

print(reachAllNodes(edges))