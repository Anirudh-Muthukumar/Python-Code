class LazyPropagation:
    def __init__(self):
        self.tree = None
        self.lazy = None
    
    def build(self, A):
        n = len(A)
        self.tree = [None] * (2*n)
        self.lazy = [0] * (2*n)

        # fill in leaf node
        for i in range(n):
            self.tree[i+n] = A[i]
        
        # Fill parents 
        for i in range(n-1, 0, -1):
            self.tree[i] = self.tree[i<<1] + self.tree[i<<1|1]
    
    def updateRangeUtil(self, si, ss, se, qs, qe, value):
        
        # Case 0: Normalize the current node
        if self.lazy[si]!=0:
            self.tree[si] += (se-ss+1) * self.lazy[si]
            if ss!=se: # Update lazy values of child
                self.lazy[si<<1] += self.lazy[si]
                self.lazy[si<<1|1] += self.lazy[si]
            self.lazy[si] = 0
        
        # Case 1: Out of bounds
        if ss>se or ss>qe or se<qs:
            return 
        
        # Case 2: Segment completely within query range
        if qs<=ss and se<=qe:
            self.tree[si] += (se-ss+1) * value
            if se!=ss:
                self.lazy[si<<1] += value 
                self.lazy[si<<1|1] += value
            return
        
        # Case 4: Partial overlap, update children
        mid = (se+ss)>>1
        self.updateRangeUtil(si<<1, ss, mid, qs, qe, value)
        self.updateRangeUtil(si<<1|1, mid+1, se, qs, qe, value)

        # Update current node
        self.tree[si] = self.tree[si<<1] + self.tree[si<<1|1]

    def updateRange(self, qs, qe, value): # Range [qs, qe]
        n = len(self.tree)>>1
        self.updateRangeUtil(1, 0, n-1, qs, qe, value)
    
    def queryRangeUtil(self, si, ss, se, qs, qe):
        # Case 0: Normalize the current node
        if self.lazy[si]!=0:
            self.tree[si] += (se-ss+1) * self.lazy[si]
            if ss!=se:
                self.lazy[si<<1] += self.lazy[si]
                self.lazy[si<<1|1] += self.lazy[si]
            self.lazy[si] = 0
        
        # Case 1: Out of bounds
        if ss>se or ss>qe or se<qs:
            return 0 
        
        # Case 2: Segment completely within the query range
        if qs<=ss and se<=qe:
            return self.tree[si]
        
        # Case 3: Partial overlap
        mid = (ss+se)>>1
        return self.queryRangeUtil(si<<1, ss, mid, qs, qe) + self.queryRangeUtil(si<<1|1, mid+1, se, qs, qe)

    
    def queryRange(self, qs, qe): # Range [qs, qe]
        n = len(self.tree)>>1
        return self.queryRangeUtil(1, 0, n-1, qs, qe)
    
if __name__ == '__main__':
    lazyProp = LazyPropagation()
    arr = [18, 17, 13, 19, 15, 11, 20, 12]
    lazyProp.build(arr)
    print("Range Sum [2, 8] = ", lazyProp.queryRange(2, 8))
    print("Update range [2, 8] with value 1", lazyProp.updateRange(2, 8, 1))
    print("Range Sum [2, 8] = ", lazyProp.queryRange(2, 8))

