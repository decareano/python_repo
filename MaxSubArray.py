class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
            maxSum = float('-inf')
            currentSum = 0
            

            for i in nums:
                currentSum += i
                maxSum = max(maxSum, currentSum)
                currentSum = max(currentSum, 0)  #takes care of the negative
            return maxSum   
