class Solution:
    def countSubarrays(self, nums):
        #output == 1
        #how to make a subarray(3 elements)
        #such as the sum of the first and third element
        #are half of the second element
        
        n = len(nums)
        count = 0
        # n-2 cuz we need subs of three elements
        for i in range(n-2):
            firstE = nums[i]
            secE = nums[i+1]
            thirE = nums[i+2]
            
            if firstE + thirE == secE / 2:
                count += 1
        return count
            

myVar = Solution()
myVar.countSubarrays([1,2,1,4,1])
