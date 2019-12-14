def twoSum(nums, target):
        dict = {}
        
        for i in range(len(nums)):
            if target-nums[i] not in dict:
                print(target-nums[i])
                dict[nums[i]] = i
            else:
                return [dict[target-nums[i]], i]
                
nums = [2,7,5,8]
print(twoSum(nums, 15))
