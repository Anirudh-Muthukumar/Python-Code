t=input()
for _ in range(t):
    l=list(map(int,raw_input().split()))
    n,m=l[0],l[1]
    print abs(m-n)