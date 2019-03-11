matrix_size = int(input())
difference = 0

for i in range(matrix_size):
    row = input().split()
    for j in range(matrix_size):
        if j == i:
            pos_diag = int(row[j])
        if j == matrix_size-i-1:
            neg_diag = int(row[j])
            import pdb; pdb.set_trace()
    difference += pos_diag
    difference -= neg_diag
print(abs(difference))
