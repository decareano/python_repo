import math

ab = int(input())
likes = 0
total = 5


for i in range(ab):
    
    likes += math.floor(total/2)
    total = math.floor(total/2)*3
    
print(likes)


# for i in movie_days:
#     a = str(i)
#     c = int((a[::-1]))
#     if abs(i-c)%k == 0:
#         counter +=1
# print(counter)
