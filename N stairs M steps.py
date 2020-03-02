def count(n, m):
    res = [0] * (n+1)
    res[0] = 1
    res[1] = 1
    
    for i in range(2, n):
        j = 1
        while j<=m and j<=i:
            res[i] = res[i] + res[i-j]
            j+=1
    
    print("# of ways: ", res[n-1])



if __name__ == '__main__':
    n = 4
    m = 2
    count(n+1, m)