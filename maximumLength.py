from collections import Counter

class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        count = Counter(nums)

        res = 0
        for key in count.keys():
            if key == 1:
                total = count[key] if count[key] % 2 else count[key] - 1
            else:
                total = 0
                while count[key] >= 2 and key * key in count:
                    total += 2
                    key = key * key
                total += 1
            res = max(res, total)
        return res
        
myVar = Solution()
myVar.maximumLength([1,3,2,4])

#my efforts-no good could not get it to work

class Solution:
#     def maximumLength(self, nums):
#         count_dict = {}
#         count = 0
#         for item in nums:
            
#             if item in count_dict:
#                 count_dict[item] += 1
#             else:
#                 count_dict[item] = 1
#         i = 0
        
#         currMax = 0
#         while i < len(nums):
           
#             curr = nums[i]
#             square = curr * curr
           
#             #if square in count_dict:
              
#             if count_dict[curr] == 1:
#                     total = count_dict[curr] if count_dict[curr] % 2 else count_dict[curr] -1
#             elif count_dict[curr] >= 2 and square in count_dict: 
#                     total += 2
#             #total += 1
#             i += 1
#         res = max(currMax, total)
#         return res

#         return currMax
# myVar = Solution()
# myVar.maximumLength([5,4,1,2,2])
