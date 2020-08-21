'''
Time complexity : O(V+E)
Space complexity: O(V)
'''

import collections

class TarjanSCC:
    def __init__(self, graph, n):
        self.graph = graph
        self.n = n
        # print("Size = ", self.n)
    
    def solve(self):
        UNVISITED = -1
        self.ids = [UNVISITED] * self.n
        self.onStack = [False] * self.n 
        self.low = [UNVISITED] * self.n
        self.stack = [] 
        self.id = 0 # to label nodes
        self.sccCount = 0   # number of SCCs

        for node in range(self.n):
            if self.ids[node] == UNVISITED:
                self.dfs(node)

        return self.low  # return the array of low link values 

    def dfs(self, node):
        self.stack += node,
        self.onStack[node] = True 
        self.ids[node] = self.low[node] = self.id 
        self.id += 1
        UNVISITED = -1

        for nei in self.graph[node]:
            if self.ids[nei] == UNVISITED: 
                self.dfs(nei)
            if self.onStack[nei]: 
                self.low[node] = min(self.low[nei], self.low[node]) 
        
        # Pop all the nodes belonging to current SCC 
        if self.ids[node] == self.low[node]: 
            while self.stack:
                temp = self.stack.pop()
                self.onStack[temp] = False 
                self.low[temp] = self.ids[node]
                if temp==node:
                    break
            self.sccCount += 1 

# edges = [[1, 0], [0, 2], [2, 1], [0, 3], [3, 4]] 
edges = [[0, 1], [1, 2], [2, 0], [1, 3], [1, 4], [1, 6], [3, 5], [4, 5]]
graph = collections.defaultdict(list) 
for u, v in edges:
    graph[u] += v, 

tarjan = TarjanSCC(graph, 7)
low_links = tarjan.solve()  
links = collections.defaultdict(list) 
for ind, low in enumerate(low_links):
    links[low] += ind, 

print("Number of SCCs = ", tarjan.sccCount)
for key in links:
    print(links[key]) 
print()
