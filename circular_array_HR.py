# Complete the circularArrayRotation function below.
n, k, m = list(map(int, input().rstrip().split()))
arr = list(map(int, input().split()))
k %= n      #will work when k is greater than n --rotations bigger than elements
arr = arr[-k:]+arr[:-k]
#print(arr)
#a = a[1:]+a[:1]
#print(arr)
# #queries = []
#arr = arr[numOfRotations:]+arr[:numOfRotations]
for _ in range(m):
     print(arr[int(input().strip())])
    
# n, k, m = map(int, input().strip().split())
# arr = list(map(int, input().strip().split()))
# #k %= n

# arr = arr[1:] + arr[:1]

# for i in range(m):
#     print(arr[int(input().strip())])

