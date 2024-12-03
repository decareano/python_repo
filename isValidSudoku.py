class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        res = []
        for row in range(9):
            for col in range(9):
                elem = board[row][col]
               
                if elem != '.':
                    #we do all the checking here
                    #row, col and subgrid
                   #res += [(row, elem), (elem, col), (row // 3, col // 3, elem)]
                   res += [(row // 3, col // 3, elem)]
                   res += [(row, elem)]
                   res += [(elem, col)]
                   
                   print([(row // 3)])
                   print([(col // 3)])
                   
            print(len(res))
            print(len(set(res)))
            return len(res) == len(set(res))    
        
        # a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
        # for i in range(len(a)):
        #     for j in range(len(a[i])):
        #         print(a[i][j], end=' ')
        # print()    
myVar = Solution()
myVar.isValidSudoku(
    board =
    [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
