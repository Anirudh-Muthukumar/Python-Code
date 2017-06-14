class Queue(object):
    def __init__(self):
        self.qlist=[]
    
    def insert(self,i):
        self.qlist.append(i)
    
    def remove(self):
        if len(self.qlist)>0:
            ans=self.qlist[0]
            self.qlist.remove(ans)
            return ans
        else:
            raise ValueError()
               
#q1.insert(7)
#q1.remove()