class Solution:
    def combinationSum3(self, k, n):
        res = []
        def helper(remain, combo, next_start):
            if remain == 0 and len(combo) == k:
                res.append(list(combo))
                return
                
            elif remain < 0 or len(combo) == k:
                return 
            for i in range(next_start, 9):
                    combo.append(i+1)
                    # i is zero here and that s the reason
                    # why we do remain-i-1
                    helper(remain-i-1, combo, i+1)
                    combo.pop()
                    
        helper(n, [], 0)        
        return res
myVar = Solution()
myVar.combinationSum3(3, 7)
