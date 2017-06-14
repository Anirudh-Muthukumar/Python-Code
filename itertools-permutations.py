import itertools
l=raw_input().split()
str,n=l[0],int(l[1])
#for i in itertools.permutations(str,n):
 #   print i
k=list(itertools.permutations(str,n))
k.sort()
for i in k:
    l=''
    l+=i[0]
    l+=i[1]
    print l