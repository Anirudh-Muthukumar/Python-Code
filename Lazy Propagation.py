class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [None] * (2*n)
        self.lazy = [0] * (2*n)


    def build(self, A):
        n = self.n 
        # fill in the leaf nodes
        for i in range(n):
            self.tree[i+n] = A[i]
        
        # fill the parents from N-1 to 0
        for i in range(n-1, 0, -1):
            self.tree[i] = self.tree[i<<1] + self.tree[i<<1 | 1] # node at position i will have children at 2i and 2i+1

    def query(self, l, r):  # Range [l, r)
        res = 0
        l += self.n 
        r += self.n 

        while l<r:
            if (l&1):
                res += self.tree[l]
                l += 1
            
            if (r&1):
                r -= 1
                res += self.tree[r]
            l >>= 1
            r >>= 1

        return res
    
    def update(self, p, value):     # update position 'p' with given value
        n = self.n
        # update leaf node
        self.tree[p+n] = value
        
        # parent of a node : i>>1 
        # sibling of a node: i^1
        i = p+n 
        # Update parents and move upwards
        while i>1:
            self.tree[i>>1] = self.tree[i] + self.tree[i^1]
            i >>= 1

        return

    def display(self):
        level = 0
        ct = 0
        for i in range(2*self.n):
            print(self.tree[i], end = ' ')
            ct+=1
            if (ct==2**level):
                print()
                level+=1
        print()
    
    def updateRangeUtil(self, si, ss, se, qs, qe, diff):
        
        # Case 0: Normalize the current node
        if self.lazy[si]!=0:
            self.tree[si] += (se-ss+1) * self.lazy[si]
            if se!=ss: # if not a leaf node, update children values
                self.lazy[si<<1] += self.lazy[si]
                self.lazy[si<<1|1] += self.lazy[si]
            self.lazy[si] = 0
        
        # Case 1: Out of range
        if ss>se or ss>qe or se<qs:
            return 
        
        # Case 2: Segment tree completely within range
        if qs<=ss and se<=qe:
            self.tree[si] += (se-ss+1) * diff 
            if se!=se: # if not a leaf node, update children values
                self.lazy[si<<1] += diff
                self.lazy[si<<1|1] += diff
            return 
        
        # Case 3: Partial overlap -> recur for children
        mid = (ss+se)>>1 
        self.updateRangeUtil(si<<1, ss, mid, qs, qe, diff)
        self.updateRangeUtil(si<<1|1, mid+1, se, qs, qe, diff)

        # if(si==3):
        #     print(self.tree[si], " = ", self.tree[si<<1], " + ", self.tree[si<<1|1])
        # After updating children, update node value
        self.tree[si] = self.tree[si<<1] + self.tree[si<<1|1]

        # if(si==3)
        # print("Tree index ", si , ": ", self.tree[si])

    
    def updateRange(self, qs, qe, value): # Update range [qs, qe]
        self.updateRangeUtil(1, 0, self.n-1, qs, qe, value)
    

    def queryRangeUtil(self, si, ss, se, qs, qe):
        
        # Case 0: Normalize the current node
        if self.lazy[si]!=0:
            self.tree[si] += (se-ss+1) * self.lazy[si]
            if ss!=se:
                self.lazy[si<<1] += self.lazy[si]
                self.lazy[si<<1|1] += self.lazy[si]
            self.lazy[si] = 0
        
        # Case 1: Outside range
        if se < qs or ss > qe:
            return 0
        
        # Case 2: Segment tree completely within range
        if qs<=ss and se<=qe:
            return self.tree[si]
        
        # Case 3: Partial overlap
        mid = (ss+se)>>1
        return self.queryRangeUtil(si<<1|1, mid+1, se, qs, qe) + \
                self.queryRangeUtil(si<<1, ss, mid, qs, qe)


    def queryRange(self, qs, qe):
        return self.queryRangeUtil(1, 0, self.n-1, qs, qe)

if __name__ == '__main__':
    # arr = [18, 17, 13, 19, 15, 11, 20, 12, 33, 25]
    arr = [1,2,3,4]
    segTree = SegmentTree(len(arr))
    segTree.build(arr)
    segTree.display()
    # print("Range Sum = ", segTree.query(2, 9))
    # segTree.update(5, 12)
    print("Range Sum = ", segTree.query(0, 3)) # [0, 2]

    # Increment range [0, 2] by 10
    segTree.updateRange(0, 2, 10)
    print("Updated range [0, 2] with val 10")
    print("\nNew tree : ")
    segTree.display()
    print("\nNew Range sum [0, 2] = ", segTree.queryRange(0, 2))
    
    # Increment range [0, 2] by 10
    segTree.updateRange(0, 2, 10)
    print("\nUpdated range [0, 2] with val 10")
    print("\nNew tree : ")
    segTree.display()
    print("\nRange sum [0, 2] = ", segTree.queryRange(0, 2))

