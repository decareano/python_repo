
t = int(input())
for i in range(t):
    n, m, s = input().split()
    n,m,s = [int(n), int(m), int(s)]
    #ab = m + s - 2%n + 1 
    ab = (m + s - 1)%n
    if ab == 0:
        print(n)
    else:
         print(ab)
