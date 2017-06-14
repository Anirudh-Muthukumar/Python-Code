def prime(n):
    for i in range(2,(n/2)+1):
        if n%i==0:
            return 0
    return 1
def count(n):
    ct=0
    for i in range(2,n):
        if prime(i):
            ct+=1
    return ct
n=input()
for _ in range(n):
    t=input()
    print count(t)
        