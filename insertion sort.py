def insertion(a):
    ct=0
    for i in range(1,len(a)):
        j=i-1
        temp=a[i]
        while temp<a[j] and j>=0:
            a[j+1]=a[j]
            j-=1
            ct+=1
        a[j+1]=temp
        
    print ct

def quick(a,first,last,ct):
    ct1=ct
    if first<last:
        pivot=i=first
        j=last
        while i<j:
            while ( a[i]<=a[pivot] and i<last ):
                i+=1
            while a[j]>a[pivot]:
                j-=1
            if i<j:
                a[i],a[j]=a[j],a[i]
                
        a[pivot],a[j]=a[j],a[pivot]
        ct1+=2
        quick(a,first,j-1,ct1)
        quick(a,j+1,last,ct1)
        return ct1
                
l=list(map(int,raw_input('Enter nos. : ').split()))
#insertion(l)
print quick(l,0,len(l)-1,0)

