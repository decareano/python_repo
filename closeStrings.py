class Solution:
    
    def closeStrings(self, word1, word2):
    #stores the count of the i-th letter
       freq1 = [0] * 26
       freq2 = [0] * 26
       
       for ch in word1:
       #for i, ch in enumerate(word1): #cannot make it work
           # function order returns the ch - a ascii
           # code for character and their numbers
           freq1[ord(ch) - ord('a')] += 1
         
                
       for ch in word2:
           freq2[ord(ch) - ord('a')] += 1
       for i in range(26):
            if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):
                return False
       #sorting freq1 and freq2
       freq1.sort()
       freq2.sort()
       
       return freq1 == freq2
       


myVar = Solution()     
myVar.closeStrings("uau", "ssx")