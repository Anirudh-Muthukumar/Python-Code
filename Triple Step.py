def tripleStep(n, lookup):
    # if n==0 or n==1:
    #     return 1
    # elif n==2:
    #     return 2
    
    # if n not in lookup:
    #     # print("here")
    #     lookup[n] = tripleStep(n-1, lookup) + tripleStep(n-2, lookup) + tripleStep(n-3, lookup)
    # # return tripleStep(n-1, lookup) + tripleStep(n-2, lookup) + tripleStep(n-3, lookup)
    # return lookup[n]
    lookup = [0] * (n+1)
    lookup[0] = 1
    lookup[1] = 1
    lookup[2] = 2

    for i in range(3, n+1):
        lookup[i] = lookup[i-1] + lookup[i-2] + lookup[i-3]

    return lookup[n]

if __name__ == '__main__':
    n = 10
    print(tripleStep(n, {}))