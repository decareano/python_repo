class Solution:
    def convert(self,  str, numRows):
        if numRows >= len(str):
            return str
        idx, d = 0, 1
        #create a numRows empty to represent rows
        #see below for implementation
        #if you do an empty array...numRows gets wiped
        
        # myRows is the iterable
        myRows = [[] for row in range(numRows)]
        
        for char in str:
            print(char)
            myRows[idx].append(char)
            if idx == 0:
                d = 1
            elif idx == numRows -1:
                d = -1
        # line below made it work. idx tracks d    
            idx += d
        # see how to setup multiple strings in an array
        # to concatenate all the strings
        # ie: you start with myRows[i] and then you keep
        # adding the other strings
        for i in range(numRows):
            myRows[i] = "".join(myRows[i])
            
        return "".join(myRows)
        
       
myVar = Solution()
myVar.convert("PAYPALISHIRING", 3)
