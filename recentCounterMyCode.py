#instance method here or a function defined inside a class
from collections import deque 
class RecentCounter:
    #constructor
    def __init__(self):
        self.counter = 0
        self.queue = deque()
        
    def ping(self, t):
        #need to add one to the queue otherwise is empty
        #when element is less than t-3000 popleft
        self.queue.append(t)
        
        while self.queue[0] < t-3000:
            
                #self.counter += 1
                self.queue.popleft()
                self.counter -= 1
        else:
                self.counter += 1
        return self.counter       

myVar = RecentCounter()
param1 = myVar.ping(1) #calling ping with t param
param2 = myVar.ping(100)
param3 = myVar.ping(3001)
param4 = myVar.ping(3002)          


#this solution is not as elegant as the one before but
#it makes sense to me and I am using it. 
