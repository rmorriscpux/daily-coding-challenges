'''
A graph is minimally-connected if it is connected and there is no edge that can be removed while still leaving the graph connected.
For example, any binary tree is minimally-connected.

Given an undirected graph, check if the graph is minimally-connected.
You can choose to represent the graph as either an adjacency matrix or adjacency list.
'''

from typing import List

def isMinimallyConnected(graph: List[List[int]]):
    # Step 1: Ensure that the graph is completely connected.
    def isFullyConnected(graph: List[List[int]], node_index: int, connected_nodes: set):
        for i in range(0, len(graph[node_index])):
            # Add new node and recur when new connection is found. Sets are passed by reference so in the end it will contain all nodes with a direct or indirect connection to the first node.
            if graph[node_index][i] and i not in connected_nodes:
                connected_nodes.add(i)
                isFullyConnected(graph, i, connected_nodes)

        return len(connected_nodes) == len(graph)

    if not isFullyConnected(graph, 0, {0}):
        return False

    # Step 2: Determine if the graph is minimally connected.
    def rIsMinimallyConnected(graph, cur_node, prev_node, node_set):
        for i in range(0, len(graph)):
            if graph[cur_node][i]:
                # Self-connected node means the graph is not minimally connected, since this connection can be removed with no effect on the rest of the graph.
                if i == cur_node:
                    return False
                # Don't count the node immediately preceding this one.
                if i == prev_node:
                    continue
                # If we've encountered the node in the set, and it isn't the immediately preceding node, then there is a circular connection, therefore the graph is not minimally connected.
                if i in node_set:
                    return False
                # Recur, adding this node to the set, and setting it to prev_node.
                return rIsMinimallyConnected(graph, i, cur_node, node_set.union({cur_node}))

        return True

    return rIsMinimallyConnected(graph, 0, 0, set())

# Adjacency matrices below.

# Minimally connected graph
graph = [
    [0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0],
]
print(isMinimallyConnected(graph))

# Graph with circular connection.
graph = [
    [0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0],
]
print(isMinimallyConnected(graph))

# Graph with self connection.
graph = [
    [0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0],
]
print(isMinimallyConnected(graph))

# Binary Tree Style Graph
binaryTreeGraph = [
    [0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
]
print(isMinimallyConnected(binaryTreeGraph))