# Definition for singly-linked list.
class Node:
     def __init__(self, val):
         self.val = val
         self.next = next

class LinkedList:
     
     def reverseList(self):
        prev = None
        curr = self.head
        #next = None

        while curr is not None:
            # First, we set next to the next node of curr.
            next = curr.next
            #We then update curr's next pointer to point to 
            #prev (i.e., reverse the next pointer).
            curr.next = prev
            #We then set prev to curr, and curr to nxt, 
            #effectively moving the pointers one node ahead.
            prev = curr
            curr = next
        
        return prev


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

#llist.reverseList({ Node: 1, next: { Node: 2, next: { Node: 3, next: { Node: 4, next: { Node: 5, next: null} } } } })

llist.reverseList()
print(llist.head)
print(llist.head.next)
