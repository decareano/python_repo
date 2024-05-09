# Definition for a binary tree node.
# seminal exercise to understand recursion
class node:
   
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    
    def lowestCommonAncestor(self, root, p, q):
        self.res = None
        
        def dfs(node):
            if not node:
                return None
            
            if node.val == p or node.val == q:
                return node.val
            left, right = dfs(node.left), dfs(node.right) 
            if left and right:
                self.res = node
                return 
            elif left and not right:
                self.res = left
                return
            elif right and not left:
                self.res = right   
                
                    
        dfs(root)      
        return self.res
        
        
        
  
root = node(3)
root.right = node(1)
root.right.right = node(8)
root.right.left = node(0)
root.left = node(5)
root.left.left = node(6)
root.left.right = node(2)
root.left.right.left = node(7)
root.left.right.right = node(4)


myVar = Solution()
myVar.lowestCommonAncestor(root, 5, 4)
