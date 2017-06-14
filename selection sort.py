def selectionsort(L):
    for i in range(len(L)-1):
        pos=i
        j=i+1
        while(j<len(L)):
            if L[j]<L[pos]:
                pos=j
            j+=1
        L[i],L[pos]=L[pos],L[i]
    return L

l=list(map(int,raw_input("Enter the nos. : ").split()))
print selectionsort(l)