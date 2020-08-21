class UnionFind:
    def __init__(self, n):
        self.numComponents = n      # remaining components 
        self.size = n                # Total number of components
        self.parent = [i for i in range(n+1)]
        self.sizeOf = [1] * (n+1)              # Size of each component 
    
    def find(self, p): 
        '''
        Returns the parent of given component and also does path compression
        '''
        # find parent
        root = p
        while self.parent[root] != root:
            root = self.parent[root]
        
        # path compression 
        while p!=root:
            next_node = self.parent[p]
            self.parent[p] = root
            p = next_node

        return root

    def union(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y) 

        if root1 == root2: # already connected components
            return False
        elif self.sizeOf[root1] > self.sizeOf[root2]: # merge root2 to root1
            self.parent[root2] = root1
            self.sizeOf[root1] += self.sizeOf[root2]
        else: # merge root1 to root2
            self.parent[root1] = root2
            self.sizeOf[root2] += self.sizeOf[root1] 
        
        self.numComponents -= 1
        return True

edges = [[1, 2], [1, 3], [2, 3]]
edges = [[1,2], [2,3], [3,4], [4,1], [1,5]]
unionFind = UnionFind(len(edges))
for edge in edges:
    if not unionFind.union(*edge):
        print(edge)
        break
