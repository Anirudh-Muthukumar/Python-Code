def palindrome(i):
    m=i
    rev=0
    while m!=0:
        rev*=10
        rev+=(m%10)
        m/=10
    if rev==i:
        print 'Yes'
    else:
        print 'No'
        
