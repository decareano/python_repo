#this solution is O(n)
import random
class RandomizedSet:
    def __init__(self):
        self.data = []
        self.map = {}
        #key in map is element in data, val is index
    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.data)
        #add to the list. by doing so I connect
        #the dict and the list
        self.data.append(val)
        return True
    def remove(self, val: int) -> bool:
        if not val in self.map:
            return False
        backend_digit = self.data[-1]
        item_remove = self.map[val]
        print(backend_digit)
        print(item_remove)
        #look at contruct below
        self.map[backend_digit] = item_remove
        self.data[item_remove] = backend_digit
        
        self.data.pop()
        self.map.pop(val)
        return True
        
        
        
        
    def getRandom(self) -> bool:
        return random.choice(self.data)
        


random = RandomizedSet()
param_1 = random.insert(4)  #true
param_2 = random.remove(7)  #false
param_3 = random.insert(8)
param_4 = random.insert(3)  #true now 1,2
param_5 = random.insert(9)
param_6 = random.getRandom() #return either 1 or 2
param_7 = random.remove(8)   #true now only 2 left
param_8 = random.insert(5)   #false 2 already in set
param_9 = random.getRandom() #only 2 left so return 2

