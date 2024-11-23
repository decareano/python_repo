class Solution:
    def hIndex(self,  citations):
        #citations.sort()
        papers = len(citations)
        #create an array filled with zeros
        bucketCita = [0] * (papers + 1)
        #two loops one for see citations in buckets
        for citation in citations:
            bucketCita[min(citation, papers)] += 1
        #another for loop to find the h-index
        #indices are number of citations in bucketCita
        cumu_papers = 0
        #for bIndex in bucketCita[::-1]:
        for hIndex in range(papers, -1,-1):
            #see how we pass hIndex to bucketCita below
            cumu_papers += bucketCita[hIndex]
            if cumu_papers >= hIndex:
                return hIndex
       
myVar = Solution()
myVar.hIndex([3,0,6,1,5])
