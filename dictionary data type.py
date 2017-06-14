n=raw_input()
a={'',0}
while n:
    name=raw_input()
    l=''
    for i in name:
        l+=i
    a=int(raw_input())
    b=int(raw_input())
    c=int(raw_input())
    sum=a+b+c
    avg=sum/3.0
    a[l]=avg
    n-=1
check=raw_input()
l=''
for i in check:
    l+=i
if l in a:
    print a[l]
