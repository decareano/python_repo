# Binary tree node
# Breath first search
from collections import deque
class node:
     
    def __init__(self, node, left=None, right=None):
        self.left=left
        self.right=right
        self.node=node
  
    # Function to create a new
    # Binary node

#function for traversal is t()
class Solution:       
    def t(self, root):
        # pay attention to edge cases. Spend a couple of hours
        # racking my brains and the issue was with the fucking
        # edge case
        if root is None:
            return 0
        depthLevel = 0
        traversed = deque([root])
        
        while traversed:
           
            for i in range(len(traversed)):
            
                aa = traversed.popleft()
           
                if aa.left:
                    traversed.append(aa.left)
                
                if aa.right:
                 traversed.append(aa.right)
                 
            depthLevel += 1
        return depthLevel
       
root = node("A")
root.left = node("B")
root.right = node("C")
root.left.left = node("D")
root.left.right = node("G")
root.right.left = node("F")
root.right.right = node("E")
myVar = Solution()
myVar.t(root)
