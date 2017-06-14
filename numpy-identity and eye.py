import numpy
l=list(map(int,raw_input().split()))
m,n=l[0],l[1]
print numpy.eye(m,n,k=0)