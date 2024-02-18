#attempt to get driver code on my own with LL's

# Definition for singly-linked list.
# creates a 5 node with next node...OK so far
class Node:
     def __init__(self, val):
         self.val = val
         self.next = next

class LinkedList:
     def reverseList(self, myLL):
            print("hi")

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
