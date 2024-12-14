#this one
from collections import deque

class Solution:
    def updateMatrix(self, matrix: list[list[int]]) -> bool:
        rows = len(matrix) #row n
        cols = len(matrix[0])   #cols m
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        #list comprehensions
        #dist = [0 * back for _ in range(front)]
        #vis = [0 * back for _ in range(front)]
        
        q = deque()
        for i in range(0, rows):
            
            for j in range(0, cols):
                if matrix[i][j] == 0:  
                    print(matrix[i][j])
                    q.append((i,j))
                else:
                    matrix[i][j] = float('inf')
        while q:
             row, col = q.popleft()
             for dr, dc in directions:
                 #adding is sum below...
                 new_row, new_col = row + dr, col + dc
                 #print(matrix[new_row][new_col])
                 #print(matrix[rows][cols])
                 if 0 <= new_row < rows and 0 <= new_col < cols and \
                 matrix[new_row][new_col] > matrix[row][col] + 1:
                     
                    
                     matrix[new_row][new_col] = matrix[row][col]+1
                     q.append((new_row, new_col))      
        return matrix     
                
myVar = Solution()
myVar.updateMatrix(matrix = [[0,0,0],[0,1,0],[1,1,1]])
