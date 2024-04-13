class Solution:
    def subsets(self, nums):
        result = []
        n = len(nums)
        
        
        def helper(currSub, startIndex):
            #base case
            if startIndex == n:
                result.append(list(currSub))
                #need to return NONE to sequence to continue
                return
            #recursive call taking the element
            currSub.append(nums[startIndex])
            #increase startIndex
            helper(currSub, startIndex + 1)
            #recursive call w/o taking the element
            currSub.pop()
            helper(currSub,startIndex +1)
                
              
        helper([], 0)   
        return result

myVar = Solution()     
myVar.subsets([1,2,3])
