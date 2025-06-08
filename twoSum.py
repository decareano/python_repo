class Solution:
    def twoSum(self, nums, target):
        result = {}
        n = len(nums)
        for i in range(n):
            
                complement = target - nums[i]
                if complement in result:
                    return [result[complement], i]
                result[nums[i]] = i



JUNE 2025 Use this solution:

class Solution:
    def twoSum(self, nums, target):
        pair_idx = {}
        for i, num in enumerate(nums):
            print(i, num)
            if target - num in pair_idx:
                return [i, pair_idx[target - num]]
            pair_idx[num] = i
