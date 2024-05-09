# Definition for a binary tree node.
# seminal exercise to understand recursion
class node:
   
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    
    def lowestCommonAncestor(self, root, p, q):
        #result = []
       
        def dfs(node):
            if not node:
                return None
            if (node.val == p) or (node.val == q):
                print(node.val)
                #result.append(node.val)
                return node.val

            #izq = dfs(node.left)
            #der = dfs(node.right)
            #print(izq)
            #print(der)
            
            izq, der = dfs(node.left), dfs(node.right)   
            
            if izq and der:
                return node.val
            elif izq and not der:
                return izq
            elif der and not izq:
                return der
            
        #dfs(root)      
        return dfs(root)
        
        
        
  
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
