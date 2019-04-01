test_cases = int(input())

for iter in range(test_cases):
    cycles = int(input())
    if cycles%2 == 0:
        print((2**((cycles//2)+1))-1)
    else:
        print(2*((2**((cycles+1)//2))-1))
