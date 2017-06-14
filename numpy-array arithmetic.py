import numpy
l=list(map(int,raw_input().split()))
n,m=l[0],l[1]
l=[]
for _ in range(n):
    l.append(list(map(int,raw_input().split())))
A=numpy.array(l,float)
l=[]
for _ in range(n):
    l.append(list(map(int,raw_input().split())))
B=numpy.array(l,float)
print A+B
print A-B
print A*B
print A/B
print A%B
print A**B
    
