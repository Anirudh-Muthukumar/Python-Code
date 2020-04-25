'''
Find the square root of given number 'x' where 1<=x<=10^6
'''

class SquareRoot:

    def findRoot(self, n):
        lo = 1
        hi = 1000

        while lo<hi:
            x = lo + (hi-lo)//2 
            print(lo, x, hi)
            if x*x==n:
                return x 
            elif x*x>n:
                hi = x
            else:
                lo = x+1
        
        return -1


s = SquareRoot()
print("Square root of %d = %.9f" %(16129, s.findRoot(16129)))