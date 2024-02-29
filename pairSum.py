# Definition for singly-linked list.
class Node:
     def __init__(self, val = 0, next=0):
         self.val = val
         self.next = next

class LinkedList:
     
     def pairSum(self, head):
        
        slowP = head
        fastP = head
        prev = None
        

        while fastP and fastP.next:
            fastP = fastP.next.next
            # el switcharu from line 18???
            next = slowP.next
            #below code breaks the link bet 5 and 4..that's it
            #second iter prev is 5 so it connects to 4.
            slowP.next = prev
            prev = slowP   #slowP is my curr
            slowP = next
        aa = float('-inf')
        while slowP:
            
            aa = max(aa, prev.val + slowP.val)
            prev = prev.next
            slowP = slowP.next
        return aa
            
            #error on my logic....was trying to compare the 
            #two values...as in 6 and 8....but the result asks
            #for the highest value...so aa will provide that. 
       
            
llist = LinkedList()

llist.head = Node(7)
secondN = Node(4)
thirdN = Node(2)
fourthN = Node(1)

llist.head.next = secondN
secondN.next = thirdN
thirdN.next = fourthN
fourthN.next = None


llist.pairSum(llist.head)
