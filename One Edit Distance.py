def oneEdit(x, y):
    m, n = len(x), len(y)
    if abs(m-n)>1:
        return False

    count = 0
    i = 0 
    j = 0
    while i<m and j<n:

        if x[i]!=y[j]: # if characters are different
            if count==1:
                return False
            
            if m > n:
                i+=1
            elif m < n:
                j+=1
            else:
                i+=1
                j+=1
            
            count +=1
        
        else:  # characters are not equal
            i+=1
            j+=1
    
    if i<m or j<n:
        count+=1
    
    return count<=1

if __name__ == '__main__':
    str1 = "ctaasfa"
    str2 = "ctaasfa"
    print("One edit distance : ",oneEdit(str1, str2))