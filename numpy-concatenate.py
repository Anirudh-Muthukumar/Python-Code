import numpy
l=list(map(int,raw_input().split()))
N=l[0]
M=l[1]
k=[]
for _ in range(N):
    k.append(list(map(int,raw_input().split())))
A=numpy.array(k)
k=[]
for _ in range(M):
    k.append(list(map(int,raw_input().split())))
B=numpy.array(k)
print numpy.concatenate((A,B),axis=0)

