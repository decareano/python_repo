class RecentCounter:
    def __init__(self):
        
        self.queue = deque()
        
    def ping(self, t):
        self.queue.append(t)
        
        while self.queue[0] < t-3000:
            
                #self.counter += 1
                self.queue.popleft()
        return len(self.queue)      

myVar = RecentCounter()
param1 = myVar.ping(1) #calling ping with t param
param2 = myVar.ping(100)
param3 = myVar.ping(3001)
param4 = myVar.ping(3002) 
