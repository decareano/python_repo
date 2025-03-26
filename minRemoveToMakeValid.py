class Solution:
    def minRemoveToMakeValid(self, s):
        s = list(s)
        stack = []
        
      
      
        for idx, char in enumerate(s):
           if char == '(':
                stack.append(idx)
           elif char == ')':
                if stack:
                    stack.pop()
                else:
                    s[idx] = ''
        #how to pop and assign in one clean sweep  
        while stack:
             s[stack.pop()] = ''
            
        # return ''.join(s)
        return "".join(s)
            
                
        # for idx in range(len(s) -1,-1,-1):  
        #     if s[idx] == ")" and locked[idx] == '0':
        #         closeP += 1
                
        
myVar = Solution()
myVar.minRemoveToMakeValid(s = "))((")
