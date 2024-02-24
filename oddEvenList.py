# Definition for singly-linked list.
class Node:
     def __init__(self, val):
         self.val = val
         self.next = next

class LinkedList:
     
     def oddEvenList(self, head):
        #dont forget to run the edge cases
        if head == None:
            return 
        oddP = head
        evenP = head.next
        a_temp = evenP
        while evenP and evenP.next:
            #want oddP.next to jump two nodes to 3
            oddP.next = oddP.next.next
            oddP = oddP.next
            #print(oddP.next.val)
            #print(oddP.val)
            
            #ditto for evenP
            evenP.next = evenP.next.next
            evenP = evenP.next
        oddP.next = a_temp  
        return head
        
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

llist.oddEvenList(llist.head)
