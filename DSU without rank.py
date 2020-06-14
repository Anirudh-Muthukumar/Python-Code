class DSU:
    def __init__(self):
        self.parent = list(range(1001))
    
    def find(self, x):
        if self.parent[x]!=x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

dsu = DSU()
edges = [[1,2], [1,3], [2,3]]
for edge in edges:
    if not dsu.union(*edge):
        print(edge)
        break 





 