#this one
class Solution:
    def numSpecial(self, mat: list[list[int]]) -> bool:
        def get_column_sum(col_idx):
            return sum(row[col_idx] for row in mat)
       
        cSpecial = 0
        for row in mat:
                print(row)
                print(sum(row))
           
                if sum(row) == 1:
                    #below how to find index of element 1
                    col_idx = row.index(1)
                    col_sum = get_column_sum(col_idx)
                    cSpecial += col_sum == 1
        return cSpecial
       

myVar = Solution()
myVar.numSpecial(
    mat = [[1,0,0],[0,1,0],[0,0,1]])
