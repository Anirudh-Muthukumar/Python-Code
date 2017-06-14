n=input('Enter no. of primes to be found out :')
i=2
print 'First',n,'prime nos. are '
while n :
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print i
        n-=1
    i+=1
    
    
    
    