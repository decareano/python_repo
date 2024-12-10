class Solution:
    def searchMatrixTwo(self, matrix: list[list[int]], target: int) -> bool:
                
                col = 0
                leftSide = len(matrix)-1
                #another switcharoo...why? 
                while leftSide >= 0 and col <= len(matrix[0])-1:
                    cell = matrix[leftSide][col]
                    if cell > target:
                        cell = matrix[leftSide-1][col]
                        leftSide -= 1
                    #elif cell <= target:
                    if cell <= target:
                        cell = matrix[leftSide][col]
                        col += 1
                    if cell == target:
                        return True
                return False
                    
                  
                
myVar = Solution()
myVar.searchMatrixTwo(
    #matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5)
    matrix =[[5],[6]], target = 6)
