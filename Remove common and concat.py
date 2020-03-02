t = int(input())
for i in range(0,t):
    s1 = input()
    s2 = input()
    ans2 = ""
    for i in s1:
        if i in s2:
            continue
        else:
            ans2 += i
    for i in s2:
        if i in s1:
            continue
        else:
            ans2 += i
    if len(ans2)>0:
        print(ans2)
    else:
        print("-1")
