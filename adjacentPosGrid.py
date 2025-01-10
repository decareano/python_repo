# python code to implement the approach
 
# Function to check whether
# position is valid or not
 
 
def isValidPos(i, j, n, m):
 
    if (i < 0 or j < 0 or i > n - 1 or j > m - 1):
        return 0
    return 1
 
 
# Function that returns all adjacent elements
def getAdjacent(arr, i, j):
 
    # Size of given 2d array
    n = len(arr)
    m = len(arr[0])
 
    # Initialising a vector array
    # where adjacent element will be stored
    v = []
 
    # Checking for all the possible adjacent positions
    if (isValidPos(i - 1, j - 1, n, m)):
       
        v.append(arr[i - 1][j - 1])
    if (isValidPos(i - 1, j, n, m)):
        v.append(arr[i - 1][j])
    if (isValidPos(i - 1, j + 1, n, m)):
        v.append(arr[i - 1][j + 1])
    if (isValidPos(i, j - 1, n, m)):
        v.append(arr[i][j - 1])
    if (isValidPos(i, j + 1, n, m)):
        v.append(arr[i][j + 1])
    if (isValidPos(i + 1, j - 1, n, m)):
        v.append(arr[i + 1][j - 1])
    if (isValidPos(i + 1, j, n, m)):
        v.append(arr[i + 1][j])
    if (isValidPos(i + 1, j + 1, n, m)):
        v.append(arr[i + 1][j + 1])
 
    # Returning the vector
    return v
                
if __name__ == "__main__":
 
    # Given vector array
    arr = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
    x, y = 0,0
 
    # Function call
    ans = getAdjacent(arr, x, y)
 
    # Print all the adjacent elements
    for i in range(0, len(ans)):
        print(ans[i], end=" ")
