import numpy

n=input()
l=[]

for _ in range(n):
    l.append(list(map(int,raw_input().split())))
A=numpy.matrix( (l) )
print A

l=[]
for _ in range(n):
    l.append(list(map(int,raw_input().split())))
B=numpy.matrix( (l) )

print A*B