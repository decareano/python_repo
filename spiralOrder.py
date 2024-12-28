#this one
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        
       
        while top <= bottom and left <= right:
           
                for elem in range(left, right+1): 
                    result.append(matrix[top][elem])
                    print(matrix[left][right], matrix[top][left], \
                    matrix[top][elem])
                top += 1
                
                for elem in range(top, bottom+1):
                    print(elem)
                    result.append(matrix[elem][right])
                    
                right -= 1
                if top <= bottom:
                    
                    #trick is to fit the "elem" so it can loop
                    for elem in range(right, left-1, -1):
                        print(matrix[right])
                        print(matrix[left-1])
                        result.append(matrix[bottom][elem])
                    
                    bottom -= 1
                
                if left <= right:
                    
                    for elem in range(bottom, top-1, -1):
                        print(matrix[bottom])
                        print(matrix[top-1])
                        print(matrix[-1])
                        result.append(matrix[elem][left])
                    left += 1
                    
        return result            
                
myVar = Solution()
myVar.spiralOrder(
    matrix = [[1,2,3],[4,5,6],[7,8,9]])
