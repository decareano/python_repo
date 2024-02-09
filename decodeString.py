class Solution:
    def decodeString(self, s):
        stack = []
         
        for char in s:
            
            if char != ']':
                stack.append(char)
            else: 
                res = ''
                
                while stack[-1] != '[':
                    res+=stack.pop()
                stack.pop()
                n = ''
                while len(stack) != 0 and stack[-1].isdigit() == True:
                    n+=stack.pop()
                    # my attempt to resolve it with my own login
		    # problem is: it works if it's a single digit
		    # more than 1 digit(ie: 10) is different 
                    conversion1 = int(str(n))
                    res * conversion1
                    stack.append(res*conversion1)
                    
                    
                ''.join([word[::-1] for word in stack])
                
        #>>> a = ['a', 'b', 'c', 'd']
        #>>> ''.join(a)
        #'abcd'
        return ''.join([word[::-1] for word in stack])
        
myVar = Solution()     
myVar.decodeString("10[leetcode]")
