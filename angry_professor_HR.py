#!/usr/bin/py
t = int(input())
for _ in range(t):
    cancl, cancl1 = map(int, input().split())
    arrivals = map(int, input().split())
    for j in arrivals:
        if j <= 0:
            cancl1 -= 1
    if cancl1 <= 0:
        print("NO")
    else:
        print("YES")
