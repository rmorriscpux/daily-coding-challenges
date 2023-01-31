'''
Write an algorithm that computes the reversal of a directed graph. For example, if a graph consists of A -> B -> C, it should become A <- B <- C. 
'''

from collections import namedtuple

Edge = namedtuple('Edge', ['start', 'end'])

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = set()

    def __repr__(self):
        return "Nodes: " + repr(self.nodes) + "\nEdges: " + repr(self.edges)

    def addNode(self, new_node: str):
        self.nodes.add(new_node)
        return self

    def addEdge(self, start: str, end: str):
        try:
            assert self.nodes.issuperset({start, end})
        except AssertionError:
            print(f"Nodes {start} and/or {end} not found in graph.")
        else:
            self.edges.add(Edge(start, end))
        finally:
            return self

    def getReversal(self):
        reverse_graph = Graph()
        reverse_graph.nodes = self.nodes
        for e in self.edges:
            reverse_graph.addEdge(e.end, e.start)
        return reverse_graph

g = Graph()
g.addNode('a').addNode('b').addNode('c').addNode('d').addNode('e').addNode('f').addNode('g')
g.addEdge('a', 'b').addEdge('a', 'c').addEdge('b', 'd').addEdge('b', 'e').addEdge('c', 'f').addEdge('c', 'g')

print(g)
print("=====")
print(g.getReversal())