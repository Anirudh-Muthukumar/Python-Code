import numpy
l=list(map(int,raw_input().split()))
m=l[0]
l=[]
for _ in range(m):
    l.append(list(map(int,raw_input().split())))
    
A=numpy.array(l)
l=numpy.max(A,axis=0)
print l[0]