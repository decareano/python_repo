my_list = list()
if len(my_list) == 0:
    pass  # the list is empty




def first(name):
    if len(name) == 0:
        pass

first("test")


def hello():
    name = str(input("Enter your name: "))

    if name:
        print ("Hello " + str(name))

    else:
        print("Hello world")
    return

hello()
