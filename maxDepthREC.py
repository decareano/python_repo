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
    def maxDepth(self, root):
        if not root:
            return 0
        #print(self.maxDepth(root.left))
        #print(self.maxDepth(root.right))
        #print(root.left)
        #print(root.right)
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        
       
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)
myVar = Solution()
myVar.maxDepth(root)
