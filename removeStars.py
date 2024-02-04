class Solution:
    def removeStars(self, s):
        stack = []
        for char in s:
            if char != ("*"):
                stack.append(char)
            # no need to do previous....when you pop
            # the non-char *, the previous value in 
            # the stack gets deleted !!!
            elif char == ("*"):
                stack.pop()
        return ''.join(stack)


myVar = Solution()     
myVar.removeStars("leet**cod*e")
