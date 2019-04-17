n = int(input().strip())
arr = list(map(int, input().strip().split()))
#emptyArr = []
for i in range(n):
    
    #print(arr.index(arr.index(3)))
    #print(arr.index(arr.index(1)+1)+1)
    print(arr.index(arr.index(i+1)+1)+1)
    #print(arr.index(arr.index(i+1)))
    print(arr.index(arr.index(i+1)+1))
    #print(i)
