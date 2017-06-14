def sorted(s):
    l=list(s)
    lower=[]
    upper=[]
    even=[]
    odd=[]
    for i in l:
        if i.isdigit():
            if int(i)%2==0:
                even.append(int(i))
            else:
                odd.append(int(i))
        elif i.islower():
            lower.append(i)
        elif i.isupper():
            upper.append(i)
    
    lower.sort()
    upper.sort()
    even.sort()
    odd.sort()
    ans=''
    for i in lower:
        ans+=i
    for i in upper:
        ans+=i
    for i in even:
        ans+=str(i)
    for i in odd:
        ans+=str(i)
    print ans
sorted(raw_input())
    