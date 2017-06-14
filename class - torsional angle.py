import numpy

class angle(object):
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def dotprod(self):
        return numpy.dot(self.x,self.y)
    def modprod(self):
        return numpy.prod(numpy.mod(self.x),numpy.mod(self.y))
    def cos(self):
        return round(self.dotprod()/self.modprod(),2)

l=list(map(int,raw_input().split()))
x,y,z=l[0],l[1],l[2]
A=angle(x,y,z)
print A.cos()