import numpy

l=list(map(int,raw_input().split()))
n=l[0]
k=[]
for _ in range(n):
    l=list(map(float,raw_input().split()))
    k.append(l)
A=numpy.array(k)
print numpy.linalg.det(A)                   #to print determinant

# print numpy.linalg.inv(A)                 to print inverse