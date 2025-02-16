from collections import Counter
class Solution:
    
    def mergeArrays(self, nums1, nums2):
        #Counter is a nice tool. It adds similar keys 
        #in multiples dictionaries....all you need is import
        #dict1 = {index: item for index, item in enumerate(nums1)}
        #dict2 = {index: item for index, item in enumerate(nums2)}
        d1 = dict(nums1) 
        d2 = dict(nums2)
        both = Counter(d1)+Counter(d2)
        #using list comprehension to go back to list
        backToList = [(key, value) for key, value in both.items()]
        backToList.sort()
        return backToList



myVar = Solution()
myVar.mergeArrays(nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]])
