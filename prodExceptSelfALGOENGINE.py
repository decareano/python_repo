class Solution:
    def prodExceptSelf(self, nums):
            
            length = len(nums)
            result = [1] * length
            
            for i in range(1, length):
                #remember i-1 is the index not a substraction
                result[i] = result[i-1] * nums[i-1]
                
            # variable to combine nums and results from line
            # 10
            right = nums[-1]   #last digit nums[i]
            for i in range(length-2,-1,-1): #starts at index 2
                result[i] *= right
                #update right below
                right *= nums[i]
                
            return result    
                
#final output should be: 120,60,40,30,24       
            
      
myVar = Solution()     
myVar.prodExceptSelf([1,2,3,4])
