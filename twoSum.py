class Solution:
    def twoSum(self, nums, target):
        result = {}
        n = len(nums)
        for i in range(n):
            
                complement = target - nums[i]
                if complement in result:
                    return [result[complement], i]
                result[nums[i]] = i
