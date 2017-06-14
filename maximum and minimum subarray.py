t=input()
for _ in range(t):
    max=0
    min=0
    n=input()
    l=list(map(int,raw_input().split()))
    for i in l:
        if i>0:
            max+=i
    while(ct<2):
        for i in l[k:]: