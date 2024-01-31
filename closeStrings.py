class Solution:

  def closeStrings(self, word1, word2):
    #below creates an array with 26 slots
    #ie: [0,0,0...0]
    freq1 = [0] * 26
    freq2 = [0] * 26

    for ch in word1:
      #for i, ch in enumerate(word1): #cannot make it work
      # function order returns the ch - a ascii
      # code for character and their numbers
      
      #code line 14: The ord() function returns 
      #the number representing the unicode code 
      #of a specified character. we pass the substraction of
      #ch - ord('a') in ascii character: value 95 (lowest val)
      # +1 to account for zero array
      freq1[ord(ch) - ord('a')] += 1

    for ch in word2:
      freq2[ord(ch) - ord('a')] += 1
    for i in range(26):
      if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0
                                               and freq2[i] == 0):
        return False
    #sorting freq1 and freq2
    freq1.sort()
    freq2.sort()
    #below code is good but if you try that code on print function
    #it does not work
    if freq1 == freq2:
      print(True)
    else:
      print(False)

    
myVar = Solution()     
myVar.closeStrings("uau", "ssx")
