# Definition for a binary tree node.
# seminal exercise to understand recursion
class node:
   
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    
    def longestZigZag(self, root):
        self.goDir = 0
       
        def dfs(node, zigDir, pathLen):
            
            if node:
                self.goDir = max(self.goDir, pathLen)
                print(self.goDir)
                if zigDir:
                    #pathLen = max(maxPathLen, pathLen)
                    dfs(node.left, False, pathLen + 1)
                    dfs(node.right, True, 1)
               
                else:
                    dfs(node.left, False, 1)
                    dfs(node.right, True, pathLen + 1)
	#we dont need both path. Only one                
        #dfs(root, False, 0) 
        dfs(root, True, 0)
    
        return self.goDir
  
root = node(1)
root.right = node(1)
root.right.left = node(1)
root.right.right = node(1)
root.right.right.left = node(1)
root.right.right.right = node(1)
root.right.right.left.right = node(1)
root.right.right.left.right.right = node(1)


myVar = Solution()
myVar.longestZigZag(root)
