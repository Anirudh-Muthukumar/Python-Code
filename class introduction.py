import math
class coordinate(object):
     def __init__(self,x,y):
         self.x=x
         self.y=y
     def __str__(self):
         return '<'+self.x+','+self.y+'>'
     def distance(self,other):
         return math.sqrt((self.x+other.x)**2+(self.y+other.y)**2)

c=coordinate(3,4)
o=coordinate(0,0)
print o.distance(c)