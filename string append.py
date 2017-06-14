t=input()
for _ in range(t):
    s=raw_input()
    p=''
    dollar=0
    for i in s:
        if i not in p:
            dollar+=1
        p+=i
    print dollar