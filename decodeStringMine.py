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
              #list = []
              while len(stack) != 0 and stack[-1].isdigit() == True:
                  n+=stack.pop()
              stack.append(res*int(n[::-1]))

      #>>> a = ['a', 'b', 'c', 'd']
      #>>> ''.join(a)
      #'abcd'
      print(''.join([n[::-1] for n in stack]))
      return ''.join([n[::-1] for n in stack])

myVar = Solution()     
myVar.decodeString("50[leetcode]")
