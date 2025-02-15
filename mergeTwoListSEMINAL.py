# Definition for singly-linked list.
class Node:
    def __init__(self, value):
         self.value = value
         self.next = next

class Solution:
    
    def mergeTwoLists(self, ll1, ll2):
            
            # in the final product you are going to
            # ask to return dummy.next and that will
            # be the NEW root
            dummy = Node(0)
            curr = dummy
           
            while ll1 and ll2:
                print(ll1.value)
                print(ll2.value)
                if ll1.value > ll2.value:
                    #curr.next becomes ll2
                    curr.next = ll2
                    ll2 = ll2.next
                    print(ll2.value)
                else:
                    #curr next goes to LL1
                    #then LL1.next goes to LL1
                    
                    #below pasamos el pointer....nothing else
                    
                    curr.next = ll1
                    ll1 = ll1.next
                    #print(ll1.value)
                curr = curr.next
            if ll1:
                curr.next = ll1
            else:
                curr.next = ll2
            return dummy.next


ll1 = Solution()
ll1 = Node(1)
secondN = Node(2)
thirdN = Node(4)
ll1.next = secondN
secondN.next = thirdN
thirdN.next = None

ll2 = Solution()
ll2 = Node(1)
secondN = Node(3)
thirdN = Node(4)
ll2.next = secondN
secondN.next = thirdN
thirdN.next = None


myVar = Solution()
myVar.mergeTwoLists(ll1, ll2)
