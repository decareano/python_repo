# no division with for loops O(n) both space and memory


class Solution:
    def prodExceptSelf(self, nums):

            length = len(nums)
            result = len(nums) * [1]
            #or
            #result = [1] * length

            for i in range(1, length):
                result[i] = result[i-1] * nums[i-1]
                print(result[i])
                print(result[i-1])
                print(nums[i-1])
                #left *= nums[i]

            # 6 is there so no need to calculate it on the 
            # second time around
            # adding variable otherwise this does not work
            # cuz I need a way to multiply to the right of 
            # input arr
            rightMost = nums[-1]
            for i in range(len(nums)-2,-1,-1):
                #result[i] = result[i] * nums[i+1]
                result[i] *= rightMost
                rightMost *= nums[i]
                
                #result[i] = result[i] * nums[i]
                
            return result

myVar = Solution()     
myVar.prodExceptSelf([1,2,3,4])
