'''
Binary exponentiation also called as Exponentiation by squaring is used to calculate 
a raised to the power n ie., a^n

Time complexity: O(log n)
'''

def power(a, n):
    res = 1
    while n:
        if n&1:
            res *= a
            n -= 1
        a *= a
        n >>= 1
    return res  

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, n = map(int, input().split())
        print(power(a, n))

