#instance method here or a function defined inside a class
from collections import deque 
class RecentCounter:
    #constructor
    def __init__(self):
        
        self.queue = deque()
        
    def ping(self, t):
        #need to add one to the queue otherwise is empty
        #when element is less than t-3000 popleft 
        #and we continue adding here
        self.queue.append(t)
        
        while self.queue[0] < t-3000:
                #as long as the condition is true
                #we keep returning the length of self.queue
                #because they all fit the condition
                #until 3002 which fails the condition
                #and gets popped
                self.queue.popleft()
        return len(self.queue)    

myVar = RecentCounter()
param1 = myVar.ping(1) #calling ping with t param
param2 = myVar.ping(100)
param3 = myVar.ping(3001)
param4 = myVar.ping(3002)
