n=int(raw_input("Enter the no. : "))
ans=0;
while ans**3<abs(n):
    ans+=1
if ans**3!=abs(n):
    print str(n)+" is not a perfect cube "
else :
    if n<0:
        ans= -ans
    print str(n)+" is a perfect cube of "+str(ans)