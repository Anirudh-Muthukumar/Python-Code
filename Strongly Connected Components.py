# Kosaraju's Algorithm for Strongly Connected Components in a directed graph
# Complexity : O(V+E) using two DFS Search
# First DFS to fill the order of vertices in stack
# Reverse the stack and get transpose of Graph
# Visit the nodes based on order in stack on new graph

from collections import defaultdict

class Graph:

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)      # defaultdict to store the graph elements

    def addEdge(self, u, v):
        self.graph[u].append(v)   # adding directed edge

    def fillOrder(self, node, visited, stack):   # for filling the order in stack
        visited[node] = True
        
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.fillOrder(neighbor, visited, stack)
        
        stack.append(node)
    
    def DFSUtil(self, node, visited):           # finding SCC for each node
        visited[node] = True
        print(node, end = ' ')
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.DFSUtil(neighbor, visited)
    
    def getTranspose(self):         # find the transpose of the graph, each directed edge should be inverted
        g = Graph(self.V)
        for v in range(self.V):
            for neighbor in self.graph[v]:
                g.addEdge(neighbor, v)

        return g

    
    def findSCC(self):            # finding the SCCs for the given graph

        stack = []    # to maintain order
        visited =[ False for _ in range(self.V)]

        for v in range(self.V):                         # first find the order through DFS
            if not visited[v]:
                self.fillOrder(v, visited, stack)
        
        gr = self.getTranspose()                         # create a reversed graph

        # Mark all nodes as not visited for second DFS
        visited =[ False for _ in range(self.V)]
        
        # print(stack)
        # Now process all the nodes defined by order of stack
        while stack:
            node = stack.pop()
            # print("Node = ",node)
            if not visited[node]:
                gr.DFSUtil(node, visited)
                print()

if __name__ == '__main__':
    g = Graph(5) 
    g.addEdge(1, 0) 
    g.addEdge(0, 2) 
    g.addEdge(2, 1) 
    g.addEdge(0, 3) 
    g.addEdge(3, 4) 
    
    
    print ("Following are strongly connected components " +
                            "in given graph") 
    g.findSCC() 