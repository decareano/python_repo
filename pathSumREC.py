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
    def pathSum(self, root, targetSum):
        self.count = 0
        self.prefix_sum = {0: 1}
        self.dfs(root, targetSum, 0)
        return self.count
        
    def dfs(self, node, targetSum, curr_sum):
        if not node:
            return
        
        curr_sum += node.val
        
        #below adds to the count if curr - target not in dict
        self.count += self.prefix_sum.get(curr_sum - targetSum, 0)
        print(self.prefix_sum.get(curr_sum - targetSum, 0))
        #below adds to the dict: value and 1 meaning:
        #we found a key. after processing it, it goes to zero
        self.prefix_sum[curr_sum] = self.prefix_sum.get(curr_sum, 0) + 1
        #below runs the recursive calls
        self.dfs(node.left, targetSum, curr_sum)
        self.dfs(node.right, targetSum, curr_sum)
        
        self.prefix_sum[curr_sum] -= 1
        #sequence: once path is visited, it goes to 0
        #difficult to follow
        
  
root = node(10)
root.left = node(5)
root.right = node(-3)
root.right.right = node(11)
root.left.left = node(3)
root.left.right = node(2)
root.left.left.left = node(3)
root.left.left.right = node(-2)
root.left.right.left = None
root.left.right.right = node(1)
myVar = Solution()
myVar.pathSum(root, 8)
