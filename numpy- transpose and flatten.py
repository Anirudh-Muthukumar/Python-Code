import numpy
l=list(map(int,raw_input().split()))
k=[]  
for _ in range(l[0]):
    k.append(list(map(int,raw_input().split())))
A=numpy.array(k)
print numpy.transpose(A)
print A.flatten()