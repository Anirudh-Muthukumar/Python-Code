import numpy
l=list(map(int,raw_input().split()))
A=numpy.matrix( (l) )
l=list(map(int,raw_input().split()))
B=numpy.matrix( (l) )
print numpy.inner(A,B)
print numpy.outer(A,B)