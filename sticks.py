t=input()
for _ in range(t):
    n=input()
    l=list(map(int,raw_input().split()))
    max1,max2=0,0
    for i in l:
        if l.count(i)>=2 and i>max1:
                max1=i
            
    for i in l:
        if l.count(i)>=2 and i>max2 and i!=max1:
                max2=i
    if max1==0 and l.count(max2)>=
    :
            print "-1"
    else:
        print max1*max2 