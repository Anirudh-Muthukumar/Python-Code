def countBits(n):
    ct = 0
    while n>0:
        ct+=1
        n = n & (n-1)
    return ct

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(countBits(n))