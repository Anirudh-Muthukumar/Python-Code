from collections import Counter
shoes=input()
size=list(map(int,raw_input().split()))
t=input()
cash=0
for _ in range(t):
    c=list(map(int,raw_input().split()))
    if c[0] in size:
        cash+=c[1]
        size.remove(c[0])
        
print cash


