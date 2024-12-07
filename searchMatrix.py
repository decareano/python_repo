class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
                
                #m = len(matrix) 
                #m = len(matrix)-1
                #way to get the number of columns below
                #n = len(matrix[0]) # number of columns
                #m and n number of rows and cols
                top = 0
                bot = len(matrix)-1
                print(bot)
                while top <= bot:
                    mid = (top+bot) // 2
                    #testing boundaries of number we are looking for
                    #we found the row...now lets explore
                    #it.....
                    if matrix[mid][0] < target and matrix[mid][-1] > target:
                        break
                    elif matrix[mid][0] > target:
                        print(matrix[mid][0])
                        bot = mid - 1
                    else:
                        top = mid + 1
                #row will hold the index of the row
                # where we think the value would be
                # another binary search
                row = (top+bot) // 2
                left = 0
                #I guess len of the SINGLE row. so 4-1 =3??
                print(len(matrix[row]))
                right = len(matrix[row]) - 1
                print(right)
                #I was using a diff variable. mid1 instead 
                #of mid.....needed to use the same one
                while left <= right:
                    mid1= (left+right) // 2
                    print(mid1)
                    if matrix[row][mid1] == target:
                        return True
        
                    elif matrix[row][mid1] > target:
                        
                        right = mid - 1
                    else:
                        left = mid + 1
                return False
                
myVar = Solution()
myVar.searchMatrix(
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)
