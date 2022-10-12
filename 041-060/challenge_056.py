'''
Given an undirected graph represented as an adjacency matrix and an integer k, write a function to determine
whether each vertex in the graph can be colored such that no two adjacent vertices share the same color using at most k colors.
'''

# Adjacency Matrix - A matrix representing vertices in a finite graph.

from typing import List

def coloredVertices(graph: List[List[int]], k: int):
    def rColoredVertices(graph, k, colors):
        if len(colors) == len(graph):
            return True

        for i in range(0, k):
            colors.append(i)
            last_vertex = len(colors) - 1
            colored_neighbors = []
            colors_valid = True
            # Check that there's still a color available not taken up by any neighbors.
            for i, edge in enumerate(graph[last_vertex]):
                if edge and i < last_vertex:
                    colored_neighbors.append(i)
            for n in colored_neighbors:
                if colors[n] == colors[-1]:
                    colors_valid = False
                    break

            if colors_valid and rColoredVertices(graph, k, colors):
                return True

            colors.pop()

        return False

    return rColoredVertices(graph, k, [])

aMatrix = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
]

print(coloredVertices(aMatrix, 2))
print(coloredVertices(aMatrix, 3))
print(coloredVertices(aMatrix, 4))