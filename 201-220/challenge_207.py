'''
Given an undirected graph G, check whether it is bipartite.
Recall that a graph is bipartite if its vertices can be divided into two independent sets, U and V, such that no edge connects vertices of the same set.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.edges = set()

    def __repr__(self):
        return str(self.value)

    def addEdge(self, vertex):
        if repr(vertex) in map(lambda n: repr(n), self.edges):
            return
        self.edges.add(vertex)
        return

class Graph:
    def __init__(self):
        self.nodes = set()

    def addNode(self, new_node: Node):
        if repr(new_node) not in map(lambda n: repr(n), self.nodes):
            self.nodes.add(new_node)
        return self
    
    def getNode(self, value: str):
        for node in self.nodes:
            if repr(value) == repr(node):
                return node
        return None

    def addEdge(self, v1, v2):
        node1 = self.getNode(v1)
        node2 = self.getNode(v2)

        if node1 and node2:
            node1.addEdge(node2)
            node2.addEdge(node1)

        return self

    def isBilateral(self):
        sorted_nodes = sorted(self.nodes, key=lambda node: len(node.edges), reverse=True)
        set1, set2 = set(), set()

        for node in sorted_nodes:
            if node in set2:
                continue

            set1.add(node)

            if node.edges:
                for other_node in node.edges:
                    set2.add(other_node)

        for node in set2:
            if node.edges:
                for other_node in node.edges:
                    if other_node in set2:
                        return False

        return True