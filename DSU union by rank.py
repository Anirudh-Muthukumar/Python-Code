class DSU:
    def __init__(self):
        self.parent = list(range(1001))
        self.rank = [0] * (1001)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x == parent_y: # detected a cycle
            return False
        elif self.rank[parent_x] < self.rank[parent_y]:
            self.parent[parent_x] = parent_y 
        elif self.rank[parent_y] < self.rank[parent_x]:
            self.parent[parent_y] = parent_x
        else:
            self.parent[parent_y] = parent_x
            self.rank[parent_x] += 1
        return True
            