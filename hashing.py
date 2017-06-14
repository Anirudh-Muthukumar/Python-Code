import random                                   # for random

class intdict(object):
    
    def __init__(self,numbuckets):
        self.buckets=[]
        self.numbuckets=numbuckets
        for i in range(numbuckets):
            self.buckets.append([])

    def addEntry(self,key,value):
        hashbucket=self.buckets[key%self.numbuckets]    # choosing bucket 
        for i in range(len(hashbucket)):      
            if hashbucket[i][0]==key:                   # more than one value with same key
                hashbucket[i]=(key,value)
                return
        hashbucket.append((key,value))
    
    def getValue(self,key):
        hashbucket=self.buckets[key%self.numbuckets] #choosing bucket index
        for i in hashbucket:
            if i[0]==key:                           # checking for key
                return i[1]                         # returning value of the key
        return None                                 #return None if key is not present
        
    def __str(self):
        res='{'
        for b in self.buckets:
            for i in b:
                res = res + str(i[0]) + ':' + str(i[1]) + ','
        return res[:-1]                             # res[:-1] to remove trialing comma
        
D = intdict(29)
for i in range(10):
    key=random.choice(range(10**5))
    D.addEntry(key,i)
print '\n The buckets are: '
for hashbucket in D.buckets:
    print ' ',hashbucket
                