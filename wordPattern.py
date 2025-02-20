class Solution:
    
    def wordPattern(self, pattern, s):
        mySplit = s.split()
        
        if len(pattern) != len(mySplit):
            return False
            
        #char_map = {'a': 'dog', 'b': 'cat', 'b': 'cat', 'a':'dog'}
        #my_list.sort(key=len)
        
        if len(set(pattern)) != len(set(mySplit)):
            print(len(set(pattern)))
            print(len(set(mySplit)))
            return False
            
        # #my code to attempt the mapping.
        # char_map = {'a': 'dog', 'b': 'cat', 'b': 'cat', 'a':'dog'}
        # for s in pattern:
        #     temp_str = ""
        #     for char in s:
        #         if char in char_map:
        #             temp_str += char_map[char] + " "
                
        #         return True
        # return False
        
        #correct and better code to map a char to a word:
        ref = {}
        for i in range(len(pattern)):
            #doing the negative sequence
            if pattern[i] not in ref:
                ref[pattern[i]] = mySplit[i]
            #below you prove a point by doing the negative
            #sequence. I was looking for a way to 
            #do it positively and I could not
            elif ref[pattern[i]] != mySplit[i]:
                return False
        return True
                
        


myVar = Solution()
myVar.wordPattern(pattern = "abba", s = "dog cat cat dog")

