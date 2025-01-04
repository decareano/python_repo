#this one
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        zero_rows = set()
        zero_cols = set()
         
        rows = len(matrix)
        cols = len(matrix[0])
        # run 1 to identify zeros
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        # run 2 to turn whatever into zeros - rows           
        for row in zero_rows:
            for col in range(cols):
                matrix[row][col] = 0
        # run 3 to turn whatever into zeros - cols       
        for col in zero_cols:
            for row in range(rows):
                matrix[row][col] = 0
                
                
                
myVar = Solution()
myVar.setZeroes(
    matrix = [[1,1,1],[1,0,1],[1,1,1]])
