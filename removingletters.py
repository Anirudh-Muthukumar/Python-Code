def tolist(letters):
  import string
  s=string.ascii_lowercase 
  ans=''
  for l in s:
     ans+=l
  for l in ans:
      if l in letters:
           ans+=''
      else:
           ans+=l
  return ans

print tolist(['a','b','c'])