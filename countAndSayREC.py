# playing with append instead of using suffix[i] = prefix/suffix but I need to reverse the list which takes time
class Solution:
    def countAndSay(self, n):
        if n == 1:
            return "1"
        
        s = self.countAndSay(n-1)
        pinga = len(s)
        
        
        i = 0
        myStr = ""
        
        while i < pinga:
            number = s[i]
            countChars = 0
            while i < pinga and s[i] == number:
                
                countChars += 1
                i += 1
            #trick happens here
            myStr += str(countChars) + number
            
        return myStr
        
        
    # def countAndSay(self, n):
    #     s = "1"
    #     for i in range(n-1):
    #         # s becomes the result of whatever digit(s) 
    #         # you are processing. in this case "num" becomes 11
    #         s = self.numToSay(s)
    #     return s
myVar = Solution()     
myVar.countAndSay(7)
