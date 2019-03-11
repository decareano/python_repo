n = int(input())
grades_item = []

def gradingStudents(grades_item):
    for i in range(n):
        grades_item = int(input())
        if grades_item < 38:
                print(grades_item)
        elif (grades_item % 5) >= 3:
                print(grades_item + 5 - (grades_item % 5))
        else:
            print(grades_item)

result = gradingStudents(grades_item)
