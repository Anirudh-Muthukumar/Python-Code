primes = []
is_prime = [True] * (10**7+10) 

def sieve():
    maxN = 10**7
    for i in range(3, maxN+1, 2):
        if is_prime[i]:
            for j in range(i*i, maxN+1, i):
                if is_prime[j]:
                    is_prime[j] = False
    
    primes.append(2)
    for j in range(3, maxN+1, 2):
        if is_prime[j]:
            primes.append(j)
    print(len(primes))


def primeFactorization(N):
    i = 0
    print(' = ', end = ' ')
    while primes[i]*primes[i]<=N:
        if N % primes[i]==0:
            ct = 0
            while N % primes[i] == 0:
                ct += 1
                N //= primes[i]
            print('(', primes[i], '^', ct, ')', end = ' ')
        i+=1

    if N > 1:
        print('(', N, '^', 1, ')')
    print()

if __name__ == '__main__':
    sieve()
    t = int(input())
    for _ in range(t):
        n = int(input())
        primeFactorization(n)
