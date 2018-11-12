#! /usr/bin/python

def printtxt(txt):
    print(txt)
    return
printtxt("hello world")


def printfood(fruit, vegi, protein):
    print("Fruit:  ", fruit)
    print("Vegi:   ", vegi)
    print("Protein:   ", protein)
    return

printfood(vegi='carrot', fruit='apple', protein="chicken")

# default args //kinda of convoluted

def printfood1(protein, fruit='apple', vegi='carrot'):
    print("Fruit:  ", fruit)
    print("Vegi:   ", vegi)
    print("Protein:   ", protein)
    return

printfood1('chicken', vegi='potato')

a = 'data'
def run():
    global a
    b = 2
    a = a + a
    b = b + b
    print(b)
run()
print(a)

