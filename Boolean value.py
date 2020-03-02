t = int(input())
for i in range(t):
    s = input()
    a = 0
    b = 0
    step = 1
    ans = int(s[0])
    for i in range(2,len(s),step):
        if s[i]=="0" or s[i]=="1":
            if s[i-1]=="A":
                b = int(s[i])
                ans = (ans and b)
            elif s[i-1]=="B":
                b = int(s[i])
                ans = (ans or b)
            elif s[i-1]=="C":
                b = int(s[i])
                ans = (ans ^ b)
    print(ans)
