t=input()
for _ in range(t):
    n=input()
    l=list(map(int,raw_input().split()))
    for i in range(len(l)):
        if l[i]<l[i+1]:
            #print l[i],l[i+1]
            break;
    for j in range(len(l)):
        if l[len(l)-j-1]<l[len(l)-j-2]:
           # print l[len(l)-j-1],l[len(l)-j-2]
            break
    if i==len(l)-j-1:
        print 'Yes'
    else:
        print 'No'