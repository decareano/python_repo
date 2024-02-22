# Definition for singly-linked list.
class Node:
     def __init__(self, val):
         self.val = val
         self.next = next

class LinkedList:
     
     def deleteMiddle(self, head):
        #initialize
        slowP = head
        fastP = head.next
        
        while fastP.next != None and fastP.next.next != None:
            #now move  it along....takes a while 
            #to understand this logic
            fastP = fastP.next.next
            slowP = slowP.next
            #below logic: slowP has val 2 so slowP.next has val
            #3(one to be deleted. by assigning slowP.next.next 
            #to slowP.next we are deleting the link bet 2 and 3
            #twisted code !!!!!!!!!!!!!!!!!! we are not deleting it
            #we just broke the link
        slowP.next = slowP.next.next
        print(slowP.next)
        print(slowP.next.next.val)
        return head
            
        
        
        #racking my brains with the driver code
        #no need to do so...since I already
        #have the LL already define so I can pass
        #"head" to the method oddEvenList
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
llist.deleteMiddle(llist.head)
