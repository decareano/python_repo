# Definition for singly-linked list.
class Node:
     def __init__(self, value):
         self.value = value
         self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head    
    def append(self, new_node):
            current = self.head
            if current:
                while current.next:
                    current = current.next
                current.next = new_node
            else:
                self.head = new_node
        
# class LinkedList know nothing about Node       
        
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)
ll = LinkedList(e1)

ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)