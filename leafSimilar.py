# Definition for a binary tree node.
# seminal exercise to understand recursion
class node:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    # would be nice to do it with 
    # a pathSum and a helper inside pathSum(no self)
    def leafSimilar(self, root, root1):
        
        res = True
        myList = []
        myList1 = []
 
        def dfs(node):
            
            if not node:
                return
            
            
            
            dfs(node.left)
            dfs(node.right)
            
            if not node.left and not node.right:
                myList.append(node.val)
                myList1.append(node.val)
                if myList == myList1:
                    return res
                
        dfs(root)  #need this for recursion to work
        # print(res)
        # return res
  
root = node(3)
root.left = node(5)
root.right = node(1)
root.left.left = node(6)
root.left.right = node(2)
root.left.right.left = node(7)
root.left.right.right = node(4)
root.right = node(1)
root.right.left = node(9)
root.right.right = node(8)
root1 = node(3)
root1.left = node(5)
root1.right = node(1)
root1.left.left = node(6)
root1.left.right = node(7)
root1.right.left = node(4)
root1.right.right = node(2)
root1.right.right.left = node(9)
root1.right.right.right = node(8)
myVar = Solution()
myVar.leafSimilar(root, root1)
