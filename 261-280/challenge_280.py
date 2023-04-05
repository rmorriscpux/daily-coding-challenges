'''
Given an undirected graph, determine if it contains a cycle.
'''

from typing import Set

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
    
    def hasCycle(self):
        def rHasCycle(cur_node: Node, last_edge: Edge=None, seen_nodes: Set[Node]=set()):
            cycle_found = False
            for e in cur_node.edges:
                # Do not count the edge used to get here.
                if e == last_edge:
                    continue
                
                next_node = e.n2 if cur_node == e.n1 else e.n1

                if next_node in seen_nodes:
                    # Back at a previously traversed node. Cycle found.
                    return True
                else:
                    # Recur to the other node on the edge, including the current node in seen_nodes.
                    cycle_found = rHasCycle(next_node, e, seen_nodes.union(set([cur_node])))
                # Check if a cycle was found in a recurred instance.
                if cycle_found:
                    return True
                
            return False
        
        # Check for every node. Disconnected nodes may exist in the graph.
        for cur_node in self.nodes:
            if rHasCycle(cur_node):
                return True
            
        return False
    
# g1 - Cycle
#
#     c
#    / \
# a-b   e-f
#    \ /
#     d

g1 = Graph()
g1.addNode('a').addNode('b').addNode('c').addNode('d').addNode('e').addNode('f')
g1.addEdge('a', 'b').addEdge('b', 'c').addEdge('b', 'd').addEdge('c', 'e').addEdge('d', 'e').addEdge('e', 'f')

print(g1.hasCycle())

# g2 - No Cycle
#
# a     e
#  \   /
#   c-d
#  /   \
# b     f

g2 = Graph()
g2.addNode('a').addNode('b').addNode('c').addNode('d').addNode('e').addNode('f')
g2.addEdge('a', 'c').addEdge('b', 'c').addEdge('c', 'd').addEdge('d', 'e').addEdge('d', 'f')

print(g2.hasCycle())