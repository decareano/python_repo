class Solution:

  def numToSay(self, nums):
    myStr = ""
    #n = len(nums)
    i = 0
    resArr = []
    while i < len(nums):
      number = nums[i]

      myCount = 0
      while i < len(nums) and number == nums[i]:
        myCount += 1
        i += 1
      myStr = str(myCount) + number
      resArr.append(list(myStr))
    print(resArr)
    return resArr

  #from countAndSay I called numToSay function
  def countAndSay(self, n):
    bb = list(n)

    #for i in range(len(bb)-1):
    #s = bb
    bb = self.numToSay(bb)
    #return bb


myVar = Solution()
myVar.countAndSay("223314444411")
