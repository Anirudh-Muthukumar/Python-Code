from itertools import combinations
t=input()
for _ in range(t):
    str=list(map(int,raw_input().split()))
    m=str[1]
    l=list(map(int,raw_input().split()))
    ct=1
    max=0
    while ct<=len(l):
        for i in list(combinations(l,ct)):
            if sum(i)%m>max:
                max=sum(i)%m
        ct+=1
    print max
    
