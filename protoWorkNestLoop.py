list1=[[2, 1, 2, 3, 4],
         [0, 4, 5],
         [1, 8, 9]]
x = []

for i in range(len(list1)):
    print(i, list1[i])
    for j in range(len(list1)):
        #list1 by itself is the subarray
        #list1[j][i] is the value at that cell!!!
        print(j, list1[j])
        print(list1[j][i], end=" ")


results:

0 [2, 1, 2, 3, 4]
0 [2, 1, 2, 3, 4]
2 1 [0, 4, 5]
0 2 [1, 8, 9]
1 1 [0, 4, 5]
0 [2, 1, 2, 3, 4]
1 1 [0, 4, 5]
4 2 [1, 8, 9]
8 2 [1, 8, 9]
0 [2, 1, 2, 3, 4]
2 1 [0, 4, 5]
5 2 [1, 8, 9]
9
