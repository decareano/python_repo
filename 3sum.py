class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        
        return res

myVar = Solution()
myVar.threeSum([-1, 0, 1, 2, -1, -4])

#solution [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]


# made some notes to the code:

# def threeSum(self, nums):
#         nums.sort()
#         res = []
#         # not clear on line 8 as it relates to line 23
#         for i in range(len(nums)):
#             # to avoid the same number we skip it and
#             # continue to move j until we found a new
#             # number
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             j = i + 1
#             k = len(nums)-1
#             while j < k:
#                 total = nums[i] + nums[j] + nums[k]
#                 if total == 0:
#                     res.append([nums[i] + nums[j] + nums[k]])
#                 elif total < 0:
#                     j = j + 1
#                 else:
#                     if total > 0:
#                         k = k-1
#                 #need this to update while loop
#                 j += 1  
#                 # avoid duplicates triplets
#                 while nums[j] == nums[j-1] and j < k:
#                     j += 1
#         return res
