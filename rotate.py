#this one
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        matrixLen = len(matrix)
        
        # below I flipped it. but the whole exercise gets me back
        # what I had in the first place
        #7,8,9
        #4,5,6
        #1,2,3
        # for i in range(matrixLen):
        #     for j in range(matrixLen):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        #         print(matrix[j])
        #         print(matrix[i])
        #         print(matrix[i][j])
        #         print(matrix[j][i])
        matrix.reverse()
        #below explain: need to define limits to the looping
        #ie: top row and bottom row
        topP = 0
        botP = matrixLen-1
        
        for i in range(matrixLen):
            for j in range(i+1, matrixLen):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                print(matrix[j])
                print(matrix[i])
                print(matrix[i][j])
                print(matrix[j][i])
        print(matrix)
        
        #below I am gonna do the diagonal
        # for i in range(matrixLen):
        #     for j in range(i, matrixLen):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        #         print(matrix[j])
        #         print(matrix[i])
        #         print(matrix[i][j])
        #         print(matrix[j][i])
        # matrix.reverse()
        # print(matrix)
        
        #the diagonal should resolve the 90 degrees
        #and this for the reverse
        # for loop for i in range(n):
            #matrix[i].reverse()
        
myVar = Solution()
myVar.rotate(
    matrix = [[1,2,3],[4,5,6],[7,8,9]])
