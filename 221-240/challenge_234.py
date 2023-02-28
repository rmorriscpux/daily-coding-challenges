'''
Recall that the minimum spanning tree is the subset of edges of a tree that connect all its vertices with the smallest possible total edge weight.
Given an undirected graph with weighted edges, compute the maximum weight spanning tree.
'''

class Node:
    def __init__(self, val):
        self.val = val

    def __hash__(self):
        return hash(self.val)

    def __repr__(self):
        return str(self.val)

class Edge:
    def __init__(self, target, weight):
        self.target = target
        self.weight = weight

    def __hash__(self):
        return hash(self.target)

    def __repr__(self):
        return "-{}-> {}".format(self.weight, self.target)

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = dict()

    def addNode(self, node):
        self.nodes.add(node)
        self.edges[node] = set()

        return self

    def addEdge(self, source, target, weight):
        if source not in self.nodes:
            self.addNode(source)
        if target not in self.nodes:
            self.addNode(target)

        self.edges[source].add(Edge(target, weight))
        self.edges[target].add(Edge(source, weight))

        return self

    def getMaxSpan(self):
        def rGetMaxSpan(start, remaining, cur_total):
            if not remaining:
                return cur_total

            totals = []
            for edge in self.edges[start]:
                if edge.target in remaining:
                    new_remaining = remaining.copy()
                    new_remaining.remove(edge.target)
                    totals.append(rGetMaxSpan(edge.target, new_remaining, cur_total + edge.weight))

            return max(totals)

        if not self.nodes:
            return 0

        all_nodes = list(self.nodes)
        max_total = 0
        for i, n in enumerate(all_nodes):
            max_total = max(max_total, rGetMaxSpan(n, all_nodes[:i] + all_nodes[i+1:], 0))
        
        return max_total

if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    
    g = Graph()
    g.addEdge(a, b, 1).addEdge(a, c, 2).addEdge(b, c, 3).addEdge(a, d, 4).addEdge(b, d, 5).addEdge(c, d, 6)

    print(g.getMaxSpan())