class Solution:
    
    def isIsomorphic(self, s, t):
        char_index_s = {}
        char_index_t = {}
        
        for i in range(len(s)):
            print(s[i])
            print(t[i])
            if s[i] not in char_index_s:
                char_index_s[s[i]] = i
            if t[i] not in char_index_t:
                char_index_t[t[i]] = i
            if char_index_s[s[i]] != char_index_t[t[i]]:
                return False
        return True
myVar = Solution()
myVar.isIsomorphic(s = "egr", t = "add")

