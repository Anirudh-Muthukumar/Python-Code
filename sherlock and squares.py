import math    
t=input()
while t:    
    l=list(map(int,raw_input().split()))
    ct=0
    step=1
    for i in range(l[0],l[1]+1,step):
        if math.floor(math.sqrt(i)) == math.ceil(math.sqrt(i)) :
            ct+=1
            step=2*math.floor(math.sqrt(i))+1
    print ct
    t-=1
        
        