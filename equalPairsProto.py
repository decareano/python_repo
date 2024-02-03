#nested loop proto with list of lists

list1=[[3,1,2,2],
         [1,4,4,5],
         [2,4,2,2],
         [2,4,2,2]]
         
#below proper syntax for nested loop
#see how to align i and j
#if I run list1[i][j] I get the horizontal row (wrong)
#if I run list1[j][i] I get the vertical column (right)
#if I run j first I iterate through the column first and 
#then the row.....as opposed to iterate through the row first
#and then the column
for i in range(len(list1)):
  for j in range(len(list1)):
      print(list1[j][i])
