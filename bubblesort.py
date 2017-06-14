def bubblesort(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
            j+=1
    print a
            
l=list(map(int,raw_input("Enter the nos. : ").split()))
bubblesort(l)