def Sieve(n):
    prime = [True] * (n+1)
    p = 2
    while p*p <=n :
        if prime[p]:
            for j in range(p*2, n+1, p):
                prime[j] = False
        p+=1
        # print(p)

    prime[0] = False
    prime[1] = False

    print("List of primes between 1 and ", n+1)

    for i in range(2, n+1):
        if prime[i]:
            print(i, end = ' ')
    
    print()

if __name__ == '__main__':
    Sieve(100)