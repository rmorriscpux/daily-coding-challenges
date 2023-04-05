'''
A bridge in a connected (undirected) graph is an edge that, if removed, causes the graph to become disconnected. Find all the bridges in a graph.
'''

class Node:
    def __init__(self, name: str):
        self.name = name
        self.edges = set()

    def __repr__(self):
        return f"Node({self.name})"
    
class Edge:
    def __init__(self, n1: Node, n2: Node):
        self.n1 = n1
        self.n2 = n2

    def __repr__(self):
        return f"Edge({self.n1.name} - {self.n2.name})"
    
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = set()

    def getNode(self, target_node: str):
        for node in self.nodes:
            if node.name == target_node:
                return node
            
        return None

    def addNode(self, node_name: str):
        if not any(map(lambda node: node.name == node_name, self.nodes)):
            self.nodes.add(Node(node_name))
        return self
    
    def addEdge(self, n1_name: str, n2_name: str):
        n1 = self.getNode(n1_name)
        n2 = self.getNode(n2_name)

        if not n1:
            n1 = Node(n1_name)
            self.addNode(n1)
        if not n2:
            n2 = Node(n2_name)
            self.addNode(n2)
        
        new_edge = Edge(n1, n2)
        n1.edges.add(new_edge)
        n2.edges.add(new_edge)
        self.edges.add(new_edge)

        return self
    
    def removeNode(self, node_name: str):
        node = self.getNode(node_name)

        if node:
            for edge in self.edges:
                if node == edge.n1 or node == edge.n2:
                    self.edges.remove(edge)
            self.nodes.remove(node)
        
        return self

    def removeEdge(self, n1_name: str, n2_name: str):
        n1 = self.getNode(n1_name)
        n2 = self.getNode(n2_name)

        if not (n1 and n2):
            raise ValueError("Nodes not found.")
        
        target_edge = None
        for edge in self.edges:
            if (n1 == edge.n1 and n2 == edge.n2) or (n1 == edge.n2 and n2 == edge.n1):
                target_edge = edge
                break

        if not target_edge:
            raise ValueError("Edge between Nodes not found.")
        
        n1.edges.remove(target_edge)
        n2.edges.remove(target_edge)
        self.edges.remove(target_edge)

        return self
    
    def findBridges(self):
        def rFindBridges(cur_node: Node, nodes_visited: set, edges_used: set):
            nodes_visited.add(cur_node)
            for edge in cur_node.edges:
                if edge in edges_used:
                    continue
                next_node = edge.n2 if cur_node == edge.n1 else edge.n1
                rFindBridges(next_node, nodes_visited, edges_used.union({edge}))
            return
        
        bridges = set()
        for edge in self.edges:
            edges_used = set([edge])
            nodes_visited = set()
            rFindBridges(edge.n1, nodes_visited, edges_used)

            if len(nodes_visited) < len(self.nodes):
                bridges.add(edge)

        return bridges

# Sample Graph
#
#   b     f
#  / \   / \
# a   d-e   h
#  \ /   \ /
#   c     g

g = Graph()
g.addNode('a').addNode('b').addNode('c').addNode('d').addNode('e').addNode('f').addNode('g').addNode('h')
g.addEdge('a', 'b').addEdge('a', 'c').addEdge('b', 'd').addEdge('c', 'd').addEdge('d', 'e').addEdge('e', 'f').addEdge('e', 'g').addEdge('f', 'h').addEdge('g', 'h')

print(g.findBridges())