from collections import deque

#this is a simple use of queue code. Nothing fancy
#just the basics.


class demo_queue:
 
  def __init__(self):
      self.queue = list()
 
  def add_demo_element(self,element):
 
# Add the above method to insert the element
 
      if element not in self.queue:
          self.queue.insert(0,element)
          return True
      return False
 
  def size(self):
      return len(self.queue)
 
myTest = demo_queue()
myTest.add_demo_element("Monday")
myTest.add_demo_element("Tuesday")
myTest.add_demo_element("Wednesday")
myTest.
print(myTest.size())
