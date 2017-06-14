num=int(input())
if(num<0):
  Neg=True
  num=abs(num)
else:
  Neg=False
if num==0:
 result='0'
while(num>0):
  result+=str(num%2)
  num/=2
if(Neg):
  print 'result is  -'+result
else :
  print 'result is '+result

    