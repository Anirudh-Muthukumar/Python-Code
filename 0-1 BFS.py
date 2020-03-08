# Given a graph of binary weights, find the shortest path from source vertex to every other vertex
# Time complexity: O(V+E) 
# Implemented using double ended queue: append vertices with weight 0 to left while others to right

from collections import deque 

class node:
    def __init__(self, to, weight):
        self.to = to
        self.weight = weight 


def addEdge(u, v, wt, edges):
    edges[u].append(node(v, wt))
    edges[v].append(node(u, wt))

def zeroOneBFS(edges, source):

    n = len(edges)
    dist = [float('inf')] * n 
    dist[source] = 0

    Q = deque()
    Q.append(source) 

    while Q:
        v = Q[0]
        Q.popleft() 
        print(len(Q))
        for i in range(len(edges[v])):
            if dist[edges[v][i].to] > dist[v] + edges[v][i].weight:
                dist[edges[v][i].to] = dist[v] + edges[v][i].weight
            
            # if weight of this edge is 0, add it to front of the queue
            if edges[v][i].weight==0:
                Q.appendleft(edges[v][i].to)
            # otherwise add it to the back of the queue
            else:
                Q.append(edges[v][i].to)

    print("Vertices \tDistance from origin")
    for i in range(n):
        print("%s \t%s" %(i, dist[i]))

if __name__ == '__main__':

    vertices = 9 
    edges = []
    for i in range(vertices):
        edges.append([]) 
        
    addEdge(0, 1, 0, edges)
    addEdge(0, 7, 1, edges) 
    addEdge(1, 7, 1, edges) 
    addEdge(1, 2, 1, edges) 
    addEdge(2, 3, 0, edges) 
    addEdge(2, 5, 0, edges) 
    addEdge(2, 8, 1, edges) 
    addEdge(3, 4, 1, edges) 
    addEdge(3, 5, 1, edges) 
    addEdge(4, 5, 1, edges) 
    addEdge(5, 6, 1, edges) 
    addEdge(6, 7, 1, edges) 
    addEdge(7, 8, 1, edges) 

    # print(edges) 

    # source node 
    source = 0

    zeroOneBFS(edges, source)