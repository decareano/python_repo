# Definition for a binary tree node.

class Solution:    
    def shiftGrid(self, grid, k):
        mR = len(grid)
        nC = len(grid[0])
        # a vector is a one dimensional array
        vector1 = [0] * mR * nC
        #we need to add two subsets: last k elements
        #and first len(grid) - k 
        
        for i in range(mR):
            for j in range(nC):
                vector1[i * nC + j] = grid[i][j]
                print(vector1[i * nC + j])
                print(grid[i][j])
        vector1 = vector1[-k:] + vector1[:-k]
        
        for i in range(mR):
            for j in range(nC):
                grid[i][j] = vector1[i*nC+j]
myVar = Solution()
myVar.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1)
