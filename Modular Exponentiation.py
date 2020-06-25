'''
Binary exponentiation also called as Exponentiation by squaring is used to calculate 
a raised to the power n ie., a^n

Time complexity: O(log n)
'''

def power(a, n, p):
    res = 1
    while n:
        if n&1:
            res = (res * a) % p
            n -= 1
        a = (a * a) % p
        n >>= 1
    return res  

