'''
The transitive closure of a graph is a measure of which vertices are reachable from other vertices.
It can be represented as a matrix M, where M[i][j] == 1 if there is a path between vertices i and j, and otherwise 0.

For example, suppose we are given the following graph in adjacency list form:

graph = [
    [0, 1, 3],
    [1, 2],
    [2],
    [3]
]
The transitive closure of this graph would be:

[1, 1, 1, 1]
[0, 1, 1, 0]
[0, 0, 1, 0]
[0, 0, 0, 1]
Given a graph, find its transitive closure.
'''

from typing import List, Set

def transitiveClosure(graph: List[List[int]]) -> List[List[int]]:
    def rTransitiveClosure(graph: List[List[int]], row: int, reachable: Set[int]):
        # All vertices are reachable; no need to continue.
        if len(reachable) == len(graph):
            return
        
        for adjacency in graph[row]:
            # Exclude self-recursion.
            if adjacency == row:
                reachable.add(adjacency)
                continue
            # Recur if the vertex hasn't been traversed yet. Add to reachable before recurring to prevent endless recursion.
            if adjacency not in reachable:
                reachable.add(adjacency)
                rTransitiveClosure(graph, adjacency, reachable)
                
        return
    
    graph_len = len(graph)
    # Check that the graph is valid: Vertex values in the graph are all within the graph range.
    assert all(map(lambda row: all(map(lambda i: 0 <= i < graph_len, row)), graph))

    tc_matrix = []
    for row_index in range(0, graph_len):
        # For every vertex, get the set of reachable vertices.
        reachable = set()
        rTransitiveClosure(graph, row_index, reachable)
        # Build out the transitive closure row based on reachable vertices for that vertex. 1 if reachable, 0 if not. 
        tc_matrix.append(list(map(lambda i: int(i in reachable), range(0, graph_len))))

    return tc_matrix

graph = [
    [0, 1, 3],
    [1, 2],
    [2],
    [3]
]

print(transitiveClosure(graph))