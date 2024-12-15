#this one
from collections import deque

class Solution:
    def updateMatrix(self, matrix: list[list[int]]) -> bool:
        rows = len(matrix) #row n
        cols = len(matrix[0])   #cols m
        # up(0, -1), right(0, 1), down(1, 0), left(-1, 0)
        
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        #you are going to fill the queue with the 
        #nested loop and then you go through the queue
        #and the different directions to get distances
        #pretty complicated for my level in the sense that
        #there are many moving parts. Have some notes on 
        #tablet as well
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
