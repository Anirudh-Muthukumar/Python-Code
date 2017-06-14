ct=0
s=raw_input()
for i in range(len(s)-3):
    a=s[i]
    for j in range(i+1,len(s)-2):
        b=s[j]
        for k in range(j+1,len(s)-1):
            if s[k]==b:
                c=s[k]
                for l in range(k+1,len(s)):
                    if s[l]==a:
                        ct+=1
print ct%(10**9+7)