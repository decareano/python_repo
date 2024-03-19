# Binary tree node
# Breath first search
from collections import deque
class node:
     
    def __init__(self, node, left=None, right=None):
        self.left=left
        self.right=right
        self.node=node
  
#function for traversal is t()
class Solution:       
    def maxDepth(self, root):
        if not root:
            return 0
        #main point in recursive function is to find a None value
        #and start backing up from there.
        #easier said than done 
        #but I am beginning to get a handle of how it's don
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
root = node(3)
root.left = node(9)
root.right = node(20)
root.left.left = node(4)
root.left.right = node(12)
root.left.right.left= node(3)
root.right.left = node(15)
root.right.right = node(7)
#root.left.right.left(3)
myVar = Solution()
myVar.maxDepth(root)
