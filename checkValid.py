class Solution:
    def checkValid(self, board: list[list[int]]) -> bool:
        n = len(board)
        
        rows = [set() for i in range(0, n)]
        cols = [set() for j in range(0, n)]
        for i in range(0, n):
            print(board[i])
            for j in range(0,n):
                print(j)
                elem = board[i][j]
                #print(i, rows[i], elem)
                #print(cols[j], elem)
                
                if elem in rows[i] or elem in cols[j]:
                    return False
                rows[i].add(elem)
                cols[j].add(elem)
            return True
                
      
myVar = Solution()
myVar.checkValid(
    board =
[[1,2,3],[3,1,2],[2,3,1]])
