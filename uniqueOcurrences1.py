from collections import Counter as cc

class Solution:
    
    def uniqueOcurrences(self, nums):
         
         freq_map = cc(nums)
         freq_set = set()
         # it is possible to create dict from list/arrays but
         # in this case we needed a count of frequencies so
         # the Counter method works well in this instance
         print(freq_set)
         print(freq_map)
         # I was using nums...incorrect
         # need to use the hash....think about it!!!!!!!
         for item in freq_map:
             print(item, '->', freq_map[item])
             # I had a hard time getting into line 17
             # until I added the ELSE statement
             # also: line 19 starts as an empty set
             # so we need to add some values (line 25) 
             # and then start to compare
             if  freq_map[item] in freq_set:
                #print(freq_map[item])
                #freq_set.add(nums[item])
                return False
             else:
                freq_set.add(freq_map[item])
                
            
         return True

myVar = Solution()     
myVar.uniqueOcurrences([1,2,2,1,1,3])