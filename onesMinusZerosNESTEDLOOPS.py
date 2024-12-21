#this one
class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> bool:
        mrow = len(grid)
        ncol = len(grid[0])
        #below I was able to deconstruct a list comprehension
        #and do it with a simple nested loop
        #note: append(0) if you want the grid filled with zeros
        #res = [[0] * ncol for _ in range(mrow)]
        res = []
        for i in range(mrow):
            res.append([])
            for j in range(ncol):
                res[i].append(0)
        
        #row.count(1) means it counts the ONES
        onesRow = [row.count(1) for row in grid]
        onesCol = [col.count(1) for col in zip(*grid)]
        for i in range(mrow):
            for j in range(ncol):
                res[i][j] = onesRow[i]+onesCol[j]-(mrow-onesRow[i])-(ncol-onesCol[j])
        return res
        
        # matrix = []
        # for i in range(5):
        # # Append an empty sublist inside the list
        # matrix.append([])
        # for j in range(5):
        # matrix[i].append(j)
        # print(matrix)

myVar = Solution()
myVar.onesMinusZeros(
    grid = [[0,1,1],[1,0,1],[0,0,1]])
