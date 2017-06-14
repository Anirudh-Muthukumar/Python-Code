n=input()
for _ in range(n):
    str=raw_input()
    for i in range(len(str)):
        if str[i]=='@':
            alice=i
        elif str[i]=='.':
            dot=i
    print 'username : ' + str[:alice] + '\twebsitename : ' + str[alice+1:dot],
    print 'extention : ' + str[dot+1:]
    

            
                
