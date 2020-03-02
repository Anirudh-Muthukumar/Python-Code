class Graph:

    def __init__(self, V):
        self.V = V
        self.adj = [ [] for i in range(V) ]   # maintaining adjacent list for all nodes in the graph
    
    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def DFSUtil(self, temp, v, visited):
        visited[v] = True
        temp.append(v)

        for neighbor in self.adj[v]:
            if not visited[neighbor]:
                self.DFSUtil(temp, neighbor, visited)
        
        return temp

    def connectedComponents(self):
        visited = [False for i in range(self.V)] # all nodes are unvisited
        cc = []
        for v in range(self.V):
            if not visited[v]:
                temp = []
                cc.add(self.DFSUtil(temp, v, visited))
        return cc

if __name__ == '__main__':
    g = Graph(5)
    g.addEdge(1,0)
    g.addEdge(2,1)
    g.addEdge(4,3)

    print(g.connectedComponents())