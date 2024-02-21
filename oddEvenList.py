# Definition for singly-linked list.
class Node:
     def __init__(self, val):
         self.val = val
         self.next = next

class LinkedList:
     
     def oddEvenList(self, a_llist):
        
        oddP = 0   #index here
        evenP = 0   #index here
            
        even_head = 0 #dont know what for yet
        
        while a_llist:
            if a_llist % 2 == 0:
                oddP += 1
            else:
               evenP += 1
        
    #  def printLL(self):
    #     current_node = self.head
    #     while(current_node):
    #         print(current_node.data)
    #         current_node = current_node.next

llist = LinkedList()


llist.head = Node(1)
secondN = Node(2)
thirdN = Node(3)
fourthN = Node(4)
fifthN = Node(5)

llist.head.next = secondN
secondN.next = thirdN
thirdN.next = fourthN
fourthN.next = fifthN
fifthN.next = None
llist.oddEvenList()
#llist.oddEvenList({ val: 1, next: { value: 2, next: { val: 3, next: { val: 4, next: { val: 5, next: null} } } } })
#llist.oddEvenList({ head: 1, next: { secondN: 2, next}})
