def print_table():
    numbers = [1,2,3,4,5]
    for i in numbers:
        print '\t' + str(i),
        print
        for i in numbers:
            print i,
            for j in numbers:
                print '\t' + str(i * j),
                print