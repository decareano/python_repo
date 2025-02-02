# Definition for singly-linked list.
class Node:
    def __init__(self, data):
         self.data = data
         self.next = next

class Solution:
    
    def rotateRight(root, k):
            curr = root
            count = 1
            if not root or  not root.next:
                return root
            
            
           
            while curr.next:
                curr = curr.next
                count += 1
            k = k % count
            print(k)
            print(k%count)
            #code below I think it makes circular
            curr.next = root
            print(root.data)
            print(curr.data)
            slow = None
            fast = root
            for i in range(count-k):
		#below is a good sample for manipulating slow and fast
		#pointers
                slow = fast
                fast = fast.next

            slow.next = None
            root = fast
            return root
            
root = Node(1)
secondN = Node(2)
root.next = secondN
secondN.next = None



    
# root = Node(1)
# secondN = Node(2)
# thirdN = Node(3)
# fourthN = Node(4)
# fifthN = Node(5)

# root.next = secondN
# secondN.next = thirdN
# thirdN.next = fourthN
# fourthN.next = fifthN
# fifthN.next = None

myVar = Solution
myVar.rotateRight(root, 1)
