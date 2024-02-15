#this is a complex exercise. not in code but in how to make 
#all the moving parts come together

from collections import deque

class Solution:
    def predictPartyVictory(self, senate):
        # did not convert the string to a list !!!!!!
        senate = list(senate)
        self.queue = deque()
        self.queue1 = deque()
        radiant = self.queue
        dire = self.queue1
        
        for char in range(len(senate)):
            # if I use self.queue() is different than if I
            # use self.queue.append("blalbla")
            if senate[char] == "R":
                self.queue.append(char)
            if senate[char] == "D":
                self.queue1.append(char)
        
        while radiant and dire: #radiant and dire are truthy val
            print(bool(radiant))
            print(bool(dire))
            #r = radiant.popleft()
            #d = dire.popleft()
           
            if radiant[0] < dire[0]:
                #could not get radiant.popleft() + len(senate)
                self.queue.append(radiant.popleft() + len(senate))
                
                #self.queue.popleft()
                self.queue1.popleft()
            else:
                self.queue1.append(dire.popleft() + len(senate))
                
                #self.queue1.popleft()
                self.queue.popleft()
        
        
        return "dire" if dire else "radiant"

myVar = Solution()
myVar.predictPartyVictory("RDDDRDRRDR")  #D will be the answer

#param1 = myVar.predictPartyVictory("RDD")
