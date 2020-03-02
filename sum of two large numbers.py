t = int(input())
for i in range(t):
    nos = list(input().split())
    x = int(nos[0])
    y = int(nos[1])
    z = x+y
    if (len(str(z))==len(str(x))):
        print (z)
    else:
        print(x)
