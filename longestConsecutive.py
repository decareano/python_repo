class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0
        for n in nums:
            #how to check if current is beginning
            #of sequence....
            if n-1 not in numSet:
                length = 1
            # n + length is the sequence number progressing 
            # properly
                while n + length in numSet:
                    length += 1
                longest= max(longest, length)
        return longest
                
myVar = Solution()
myVar.longestConsecutive([100,4,200,1,3,2, 101, 102, 100])
