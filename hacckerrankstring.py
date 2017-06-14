t=int(raw_input())
while t:
  flag=0
  s=raw_input()
  r=raw_input()
  for i in s:
     if i in r:
       flag=1
       break
  if flag:
     print 'YES'
  else:
     print 'NO'
  t-=1
