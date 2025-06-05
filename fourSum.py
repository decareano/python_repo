class Solution:
    
    def four_sum(self, nums, target):
   
        nums.sort()
        result = []
    
        i = 0
        while i < len(nums) - 3:
            print(len(nums) - 3)
            #is that 0,1,2??
            j = i + 1
            while j < len(nums) - 2:
                print(len(nums) - 2)
                left, right = j + 1, len(nums) - 1
            
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                
                    if current_sum == target:
                        quad = [nums[i], nums[j], nums[left], nums[right]]
                        result.append(quad)
                        print(f"{quad} = {current_sum}")
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
            
                j += 1
            i += 1
    
        return result

myVar = Solution()
myVar.four_sum([1,0,-1,0,-2,2], 0)

#solution [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
