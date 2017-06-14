import numpy
l=list(map(int,raw_input().split()))
n,m=l[0],l[1]
l=[]
for _ in range(n):
    l.append(list(map(int,raw_input().split())))
A=numpy.array(l,int)
print numpy.max(numpy.min(A,axis=1))