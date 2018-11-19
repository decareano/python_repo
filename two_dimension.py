#!/usr/bin/env python3

cinema = []     #empty array

for j in range(5):    # 5 columns
    column = []
    for i in range(5):  # 5 rows
        column.append(0)
    cinema.append(column)
cinema[2][2] = 1
for i in range(1, 4):
    cinema[i][3] = 1
for i in range(5):
    cinema[i][4] = 1
    
cols = len(cinema)
rows = 0
if cols:
    rows = len(cinema[0])
for j in range(rows):
    for i in range(cols):
        print(cinema[i][j], end = "")
    print()
    