n=input()
cube=lambda a: a**3
l=[]
a,b=0,1
for _ in range(n):
    sum=a+b
    l.append(cube(a))
    b,a=sum,b
print l
    