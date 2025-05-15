class Solution:
    def longestPalindrome(self, s):
        if not s:
            return ""
        def backtracking(s, left, right):
            
           
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                right - left - 1
                
        start = 0
        end = 0
                
        for i in range(len(s)):
            odd = backtracking(s, i, i)
                   
            even = backtracking(s, i, i+1)
            max_Len = max(odd, even)
                    
            if max_Len > end - start:
                start = i - (max_Len - 1) // 2
                end = i + max_Len // 2
        return s[start:end+1]    
