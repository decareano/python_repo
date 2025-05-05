#good one

class Solution:
    def combinationSum(self, candidates, target):
        res = []
        
        def helper(start_index, curr_combo, rest_target):
            #success
            if rest_target == 0:
                res.append(curr_combo.copy())
            #failure
            if rest_target < 0:
                return "invalid path"
            for i in range(start_index, len(candidates)):
                
                    curr_combo.append(candidates[i])
                    helper(i, curr_combo, rest_target - candidates[i])
                    curr_combo.pop()
            
                    
                    
                
                
        helper(0, [], target)   
        return res
myVar = Solution()
print(myVar.combinationSum([2,3,6,7], 7))
