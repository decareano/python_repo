#this solution is O(n)
# attempted a switcharu on my own but I could not get to work
import random
class RandomizedSet:
    def __init__(self):
        self.data = []
        self.myHash = {}
        #key in myHash is element in data, val is index

    def insert(self, val: int) -> bool:
        #a dict is the same as set.....for add/delete
        #so O(1)
        if val in self.myHash:
            return False
        #this is an advanced feature
        #key in myHash passes val as key and 
        #the value is the index of the array/list
        self.myHash[val] = len(self.data)
        #now we add the val to the list. 
        #we keep a dict and a list at same time
        #add value to data array/list
        self.data.append(val)
        print(self.myHash[val])
        print(len(self.data))
        return True
    def remove(self, val: int) -> bool:
        if not val in self.myHash:
            return False
        #how to code last item in a variable
        last_item = self.data[-1]
        itemToRemove = self.myHash[val]
        #switcharu.....here
        self.myHash[last_item] = itemToRemove
        self.data[itemToRemove] = last_item
        #another form of switcharu on my own...no good..
        #could not get it to work
        #self.myHash[last_item] , self.data[itemToRemove] = self.data[itemToRemove], self.myHash[last_item]
        self.data.pop()
        self.myHash.pop(val)

    def getRandom(self) -> int:
        #return random.choice(self.data)
        pass

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
