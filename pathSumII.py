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
    def pathSum2(self, root, targetSum):
        
        self.sum = 0
        myList = []
 
        def dfs(node, currNode):
            
            if not node:
                return
            
            currNode.append(node.val)
            self.sum += node.val
            
            dfs(node.left, currNode)
            dfs(node.right, currNode)
            
            if not node.left and not node.right and sum(currNode) == targetSum:
                myList.append(currNode[:])
            currNode.pop()
         
        dfs(root, [])  #need this for recursion to work
        print(myList)
        return myList
  
root = node(5)
root.left = node(4)
root.right = node(8)
root.left.left = node(11)
root.left.left.left = node(7)
root.left.left.right = node(2)
root.right.left = node(13)
root.right.right = node(4)
root.right.right.left = node(5)
root.right.right.right = node(1)
myVar = Solution()
myVar.pathSum2(root, 22)
