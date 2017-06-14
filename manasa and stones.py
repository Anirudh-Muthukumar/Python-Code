t=input()

while t:
    n=input()
    a=input()
    b=input()
    l=set()
    l.add(0)
    k=set()
    while n>1:
        for i in l:
            k.add(i+a)
            k.add(i+b)
        n-=1
        l=k
        k=set()
    for i in l:
        print i,
    print '\n'
    t-=1

    
    