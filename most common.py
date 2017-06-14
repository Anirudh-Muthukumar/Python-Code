l=list(raw_input())
check=[]
dict={}
for i in l:
    if i not in dict:
        dict[i]=1
    else:
        sum=dict[i]+1
        dict[i]=sum
ct=0
for i in sorted(dict.values(),reverse=True):
        if ct<3:
            l=''
            l+=[key for key,value in dict.iteritems() if value==i][0]
            print l,i
            del dict[l]
            ct+=1
            
        
