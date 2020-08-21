import collections

class FindBridges:
    def __init__(self, graph, n):
        self.graph = graph 
        self.n = n 
    
    def solve(self):
        UNVISITED = -1
        self.ids = [UNVISITED] * self.n 
        self.low = [UNVISITED] * self.n 
        self.visited = [False] * self.n 
        self.id = 0 
        
        for node in range(self.n):
            if self.ids[node] == UNVISITED:
                self.dfs(node, -1)
        
        return self.ids, self.low
    
    def dfs(self, node, parent):
        self.visited[node] = True
        self.ids[node] = self.low[node] = self.id 
        self.id += 1 
        UNVISITED = -1
        for nei in self.graph[node]:
            if nei == parent: # for undirected graph 
                continue
            elif not self.visited[nei]:
                self.dfs(nei, node) 
                self.low[node] = min(self.low[node], self.low[nei])
            else:
                self.low[node] = min(self.low[node], self.ids[nei])

edges = [[0,1],[1,0],[0,2],[2,0],[1,2],[2,1],[2,3],[3,2],[2,5],[5,2],[3,4],[4,3],[5,6],[6,5],[6,8],[8,6],[8,7],[7,8],[5,7],[7,5]]
graph = collections.defaultdict(list) 
for u, v in edges:
    graph[u] += v, 

bridges = FindBridges(graph, 9)
ids, low = bridges.solve()

res = []
# Bridge condition for edge a->b : id[a] < low[b]
for a, b in edges:
    if ids[a] < low[b]:
        res.append([a, b]) 

print("BRIDGES: ")
for edge in res:
    print(edge)