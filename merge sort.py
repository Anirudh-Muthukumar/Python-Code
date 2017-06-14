def mergesort(l):
    if len(l)<2:
        return list(l)
    else:
        m=int(len(l)/2)
        left=mergesort(l[:m])
        right=mergesort(l[m:])
        return merge(list(left),list(right))
        
    
def merge(left,right):
    i,j=0,0
    result=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i<len(left):
        result.append(left[i])
        i+=1
    while j<len(right):
        result.append(right[j])
        j+=1
    return result

l=list(map(int,raw_input('Enter nos. : ').split()))
print mergesort(l)
