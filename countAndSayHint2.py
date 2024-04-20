class Solution:

  def numToSay(self, nums):
    
    n = len(nums)
    i = 0
    myStr = ""
    
   
    while i < len(nums):
        number = str(nums[i])
        myStr += number
        # myCount = 0
        # while i < len(nums) and number == nums[i]:
        #     myCount += 1
        i += 1
        # myStr += number + str(myCount)        
        
        #myStr += number + str(myCount) 
        #resArr.append(list(myStr)) 
        bb = "".join(myStr)
    print(bb, end="")
    return bb
        
        

  #from countAndSay I called numToSay function
  def countAndSay(self, n):
      
  
      for i in range(len(n)):
        s = n[i]
        s = self.numToSay(s)
      
myVar = Solution()
myVar.countAndSay([['2', '2'], ['2', '3'], ['1', '1'], ['5', '4'], ['2', '1']])
