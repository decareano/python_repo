class Solution:
    def palindromicSubstrings(self, s):
       
        count = 0
        n = len(s)
        palindromes_found = []
        # Check for odd length palindromes (single center)
        for i in range(n):
            left = right = i
            while left >= 0 and right < n and s[left] == s[right]:
                palindromes_found.append(s[left:right+1])
                count += 1
                left -= 1
                right += 1
        
       
            left = i
            right = i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                palindromes_found.append(s[left:right+1])
                count += 1
                left -= 1
                right += 1        
       
        return count      
        
myVar = Solution()
myVar.palindromicSubstrings("aaa")
