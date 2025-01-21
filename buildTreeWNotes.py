# Definition for a binary tree node.
from collections import deque
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right



class Solution:
    def buildTree(self, preorder, inorder):
            preorder = deque(preorder)
        
            def build(preorder, inorder):
                #base case. Nodes to process. Empty or not
                if inorder:
                    #print(inorder)
                    idx = inorder.index(preorder.popleft())
                    root = TreeNode(inorder[idx])
                    #left part of inorder list represents
                    #nodes in the subtree (left of root) :idx
                    root.left = build(preorder, inorder[:idx])
                    print(inorder[:idx])
                    #print(preorder)
                    #print(inorder)
                    #right part of inorder list represents
                    #nodes in the subtree(right of root) idx+1:
                    root.right = build(preorder, inorder[idx+1:])
                    print(inorder[idx+1:])
                    #print(preorder)
                    #print(inorder)
                    return root

            return build(preorder, inorder)
            
            
myVar = Solution()
myVar.buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])
