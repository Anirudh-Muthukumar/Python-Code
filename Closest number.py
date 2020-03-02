t = int(input())
for i in range(t):
    l = list(input().split())
    n = int(l[0])
    m = int(l[1])
    if n%m==0:
        print (n)
    elif m>0:
        rem = n%m
        if n>0:
            neg_rem = m - rem
            if rem<neg_rem:
                print (n-rem)
            else:
                print (n+neg_rem)
        else:
            neg_rem = m - rem
            if rem>neg_rem:
                print(n+neg_rem)
            else:
                print(n-rem)
    else:
        rem = n%m
        if n>0:
            rem = abs(rem)
            neg_rem = m - rem
            if rem<neg_rem:
                print (n+rem)
            else:
                print (n-neg_rem)
        else:
            neg_rem = m - rem
