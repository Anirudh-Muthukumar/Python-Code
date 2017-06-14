n=input()
dict={}
dict2={}
ct=0
for _ in range(0,n):
    item=list(raw_input().split())
    if len(item)==2:
        if item[0] not in dict:
            dict[item[0]]=item[1]
            dict2[item[0]]=ct
            ct+=1
        else:
            sum=int(dict[item[0]])+int(item[1])
            dict[item[0]]=sum
    elif len(item)==3:
        name=item[0]+" "
        name+=item[1]
        if name not in dict:
            dict[name]=item[2]
            dict2[name]=ct
            ct+=1
        else:
            sum=int(dict[name])+int(item[2])
            dict[name]=sum
for i in dict2:
    print i,dict[i]