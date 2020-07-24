N = 10**5
is_prime = [True] * (N+10)

def generatePrime():
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(N**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, N+1, i):
                if is_prime[j]:
                    is_prime[j] = False 
    
    primes = ""
    for i in range(2, N):
        if is_prime[i]:
            primes+=str(i)
    
    print(primes[:100])

if __name__ == '__main__':
    generatePrime()
    # t = int(input())
    # for _ in range(t):
    #     n = int(input())
    #     print(is_prime[n])


