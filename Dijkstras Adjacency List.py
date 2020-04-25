import collections  

class Graph:
    def __init__(self):
        self.graph = collections.defaultdict()
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    

def minDistance(dist, SPT):
    index = -1
    mindist = float('inf')
    for i in range(len(dist)):
        if dist[i]<mindist and SPT[i]==False:
            mindist = dist[i]
            index = i   
    return index

def dijkstra(graph, src):
    n = len(graph)

    # distance array
    dist = [float('inf')] * n 
    dist[src] = 0

    # Shortest Path Tree (SPT)
    SPT = [False] * n   

    for _ in range(n):
        node = minDistance(dist, SPT)
        # smallest distance node becomes part of SPTree
        SPT[node] = True
        # print(node)
        for neighor in range(n):
            if graph[node][neighor]>0 and SPT[neighor]==False and dist[neighor] > dist[node] + graph[node][neighor]:
                dist[neighor] = dist[node] + graph[node][neighor]

    print("Vertex\tDistance")
    for i in range(n):
        print(i, dist[i])


if __name__ == '__main__':
    v = 9 # number of vertices
    edges = [ ]
    source = 0 # source vertex
    dijkstra(graph, source)