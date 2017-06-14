import numpy
str=raw_input()
array=list(map(int,raw_input().split()))
happy=0
a=list(map(int,raw_input().split()))
b=list(map(int,raw_input().split()))
for i in array:
    if i in a:
        happy+=1
    elif i in b:
        happy-=1
        
print happy