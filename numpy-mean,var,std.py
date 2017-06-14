import numpy

l=list(map(int,raw_input().split()))
n=l[0]
k=[]
for _ in range(n):
    l=list(map(int,raw_input().split()))
    k.append(l)
A=numpy.array(k)
print numpy.mean(A,axis=1)
print numpy.var(A,axis=0)
print numpy.std(A)