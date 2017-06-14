import numpy
l=list(map(int,raw_input().split()))
n,m,o=l[0],l[1],l[2]
print numpy.zeros((m,n,o),dtype=int)
print numpy.ones((m,n,o),dtype=int)