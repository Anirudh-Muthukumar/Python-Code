n=input()
for _ in range(n):
    m=[]
    l=raw_input()
    if l.isdigit() and len(l)==10:
        for i in l:
            m+=i
        if m[0]=='9' or m[0]=='8' or m[0]=='7':
            print 'Yes'
        else:
            print 'No'    
    else:
        print 'NO'