'''
In a directed graph, each node is assigned an uppercase letter.
We define a path's value as the number of most frequently-occurring letter along that path.
For example, if a path in the graph goes through "ABACA", the value of the path is 3, since there are 3 occurrences of 'A' on the path.

Given a graph with n nodes and m directed edges, return the largest value path of the graph.
If the largest value is infinite, then return null.

The graph is represented with a string and an edge list.
The i-th character represents the uppercase letter of the i-th node.
Each tuple in the edge list (i, j) means there is a directed edge from the i-th node to the j-th node.
Self-edges are possible, as well as multi-edges.

For example, the following input graph:

ABACA

[(0, 1),
 (0, 2),
 (2, 3),
 (3, 4)]

Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).

The following input graph:

A

[(0, 0)]

Should return null, since we have an infinite loop.
'''

from typing import List, Tuple
from copy import deepcopy

def getPathValue(path_string: str, edges: List[Tuple[int, int]]):
    def rGetPathValue(graph_path, node, adjacencies):
        if node in graph_path['nodes']:
            return [graph_path]

        new_graph_path = deepcopy(graph_path)
        new_graph_path['nodes'].add(node)
        if node[0] not in new_graph_path['letter_counts']:
            new_graph_path['letter_counts'][node[0]] = 0
        new_graph_path['letter_counts'][node[0]] += 1

        if node not in adjacencies:
            return [new_graph_path]

        paths = []

        for sub_node in adjacencies[node]:
            paths.extend(rGetPathValue(new_graph_path, sub_node, adjacencies))

        return paths

    # Build a list of nodes with unique IDs from the path string.
    letters = []
    node_counts = {}

    for letter in path_string:
        if letter not in node_counts:
            node_counts[letter] = 0
        else:
            node_counts[letter] += 1
        letters.append(f"{letter}{node_counts[letter]}")

    # Tie the path-node list to adjacencies based on the edges. Omit self-edges.
    adjacencies = {}
    for start, end in edges:
        if letters[start] not in adjacencies:
            adjacencies[letters[start]] = set()
        if start != end:
            adjacencies[letters[start]].add(letters[end])

    # Build a list of dictionaries containing the possible paths, using the recursive subroutine.
    paths = []
    for node in adjacencies:
        paths.extend(rGetPathValue({'nodes': set(), 'letter_counts': dict()}, node, adjacencies))

    # Get the maximum path value.
    max_value = 0
    for path in paths:
        max_value = max(max_value, max(path['letter_counts'].values()))

    return max_value if max_value > 0 else None

print(getPathValue("ABACA", [(0, 1), (0, 2), (2, 3), (3, 4)]))
print(getPathValue("A", [(0, 0)]))