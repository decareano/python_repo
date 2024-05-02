# Definition for a binary tree node.
# seminal exercise to understand recursion
class node:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def leafSimilar(self, root, root1):
       
        myList = []
       
        def dfs(node):
            
            if not node:
                return
       
            dfs(node.left)
            dfs(node.right)
            
            if not node.left and not node.right:
                myList.append(node.val)
                
                
        #trick to resolve the fact that I need two arguments
        #root and root1. we do it separately. Then we assign 
        #contents to seq1 and put the result(s) in the initialized
        #myList, then myList back to 0 and then dfs[root1]
        #and boolean to returned the result
        dfs(root) 
        seq1 = myList[:]
        myList = []
        dfs(root1) #need this for recursion to work
        
        return seq1 == myList
  
root = node(1)
root.left = node(2)
root.right = node(3)

root1 = node(1)
root1.left = node(3)
root1.right = node(2)

myVar = Solution()
myVar.leafSimilar(root, root1)
