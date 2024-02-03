#solution with nested loops..similar to recursion

class Solution:
    def equalPairs(self, grid):
        c = 0
        x = []
        for i in range(len(grid)):
            for j in range(len(grid)):
            #x=[grid[j][i] for j in range(len(grid))]
                x += [grid[j][i]]
            print(x)
           
            if x in grid:
                c = c + grid.count(x)
            x.clear()
        return c
myVar = Solution()     
myVar.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])
