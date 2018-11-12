"""
practical programming....page 135
A solution. needs refactoring

"""

values = [4,9,11]
#print(values[0])
#print(values[1])
#print(values[2])
temp = values[0]
values[0] = 0
print(values[0])
temp = values[1] - 1


for i in range(1, len(values)):
    values[i] = 2 * temp
    # line has first value 9 * 2 = 18
    # line has second value 18 * 2 = 36
    print(values[i])
    temp = values[2] - 1
    #trick happens in the loop. when you run value
    # 1 or 9 x 2 = 18 and then you run
    # temp = values[i] now temp has the value of
