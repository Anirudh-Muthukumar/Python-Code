def palindrome(i):
    m=i
    rev=0
    while m!=0:
        rev*=10
        rev+=(m%10)
        m/=10
    if rev==i:
        return True
    else:
        return False
def all(l):
    for i in l:
        if i<0:
            return False
    return True
flag=0
n=input()
l=list(map(int,raw_input().split()))
if all(l):
    for i in l:
        if palindrome(i):
            flag+=1
    if flag:
        print 'True'
    else:
        print 'False'
else:
    print 'False'