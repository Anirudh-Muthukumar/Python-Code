class SegmentTree:
    def __init__(self):
        self.tree = None
    
    def build(self, A):
        n = len(A)
        self.tree = [None] * (2*n)

        # Fill in leaf nodes
        for i in range(n):
            self.tree[i+n] = A[i]
        
        # Fill parents from N-1 to 0
        for i in range(n-1, 0, -1):
            self.tree[i] = self.tree[i<<1] + self.tree[i<<1|1]
    
    def update(self, pos, value): # Update position 'p' with value 
        n = len(self.tree)>>1
        i = pos + n 
        self.tree[i] = value 
        while i > 1:
            self.tree[i>>1] = self.tree[i] + self.tree[i^1]
            i >>= 1
    
    def query(self, l, r): # Range [l, r)
        res = 0
        n = len(self.tree)>>1
        l += n
        r += n
        while l<r:
            if l&1:
                res += self.tree[l]
                l += 1
            if r&1:
                r -= 1
                res += self.tree[r]
            l >>= 1
            r >>= 1
        return res 
    
class SegmentTree:
    def __init__(self):
        self.tree = None
    
    def build(self, A):
        n = len(A)
        self.tree = [None] * (2*n)

        # Fill in leaf nodes
        for i in range(n):
            self.tree[i+n] = A[i]
        
        # Fill parents from N-1 to 0
        for i in range(n-1, 0, -1):
            self.tree[i] = self.tree[i<<1] + self.tree[i<<1|1]
    
    def update(self, pos, value): # Update position 'p' with value 
        n = len(self.tree)>>1
        i = pos + n 
        self.tree[i] = value 
        while i > 1:
            self.tree[i>>1] = self.tree[i] + self.tree[i^1]
            i >>= 1
    
    def query(self, l, r): # Range [l, r)
        res = 0
        n = len(self.tree)>>1
        l += n
        r += n
        while l<r:
            if l&1:
                res += self.tree[l]
                l += 1
            if r&1:
                r -= 1
                res += self.tree[r]
            l >>= 1
            r >>= 1
        return res 
    
if __name__ == '__main__':
    segTree = SegmentTree()
    arr = [18, 17, 13, 19, 15, 11, 20, 12, 33, 25]
    segTree.build(arr)
    print("Range Sum [2, 8] = ", segTree.query(2, 9))
    print("Update 4th index to 5", segTree.update(4, 5))
    print("Range Sum [2, 8] = ", segTree.query(2, 9))